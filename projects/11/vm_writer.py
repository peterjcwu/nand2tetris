"""
Functions and data maps that produce virtual machine commands.
"""

# Maps a VM op command.
ops = {
    '+': 'add\n',
    '-': 'sub\n',
    '*': 'call Math.multiply 2\n',
    '/': 'call Math.divide 2\n',
    '&': 'and\n',
    '|': 'or\n',
    '<': 'lt\n',
    '>': 'gt\n',
    '=': 'eq\n',
    '~': 'not\n',
    'neg': 'neg\n'
}

# Maps a VM unary op command.
unary_ops = {
    '~': 'not\n',
    '-': 'neg\n'
}

# maps specific terms to simple VM commands
# true is NOT mapped to push constant 1 followed by a neg (-1) as described
# on page 233 in the book (2008 paperback). It is instead mapped to
# push contant 0 followed by a not (~0). This matches and make testing compatible,
# with the course's supplied JackCompiler (v 2.5).
terms = {
    'true': 'push constant 0\nnot\n',
    'false': 'push constant 0\n',
    'null': 'push constant 0\n',
    'this': 'push pointer 0\n'
}


def write_push(segment: str, index: int):
    assert segment in {"constant", "argument", "local", "static", "this", "that", "pointer", "temp"}
    return f'push {segment} {index}\n'


def write_pop(segment: str, index: int):
    assert segment in {"constant", "argument", "local", "static", "this", "that", "pointer", "temp"}
    return f'pop {segment} {index}\n'


def write_arithmetic(command):
    """
    Writes a VM arithmetic command.
    Accepts an op command: +, -, *, /, &, |, <, >, =
    Or a unary op command: -, ~
    """

    if command in unary_ops:
        return unary_ops[command]

    return ops.get(command)


def write_term(command):
    """ Writes simple terms: true, false, null, this"""
    return terms[command]


def write_string(string):
    """
    Writes String constant using the OS constructor String.new(length)
    and the OS method String.appendChar(nextChar).
    """

    code = 'push constant ' + str(len(string)) + '\n'
    code += 'call String.new 1\n'

    for char in string:
        code += 'push constant ' + str(ord(char)) + '\n'
        code += 'call String.appendChar 2\n'

    return code


def write_label(label: str):
    """ Writes a VM label command. Accepts label. """
    return f'label {label}\n'


def write_goto(label):
    """ Writes a VM goto command. Accepts label. """
    return f'goto {label}\n'


def write_if(label) -> str:
    """ Writes a VM If-goto command. Accepts label. """
    return f'if-goto {label}\n'


def write_call(class_name: str, func_name: str, num_args: int) -> str:
    """ Writes a VM call command. Accepts class name, function name and number of arguments. """
    return f'call {class_name}.{func_name} {num_args}\n'


def write_function(class_name, func_name, num_args) -> str:
    """ Writes a VM function command. Accepts name and number of local variables. """
    return f'function {class_name}.{func_name} {num_args}\n'


def write_return() -> str:
    """ Writes a VM return command. """
    return 'return\n'
