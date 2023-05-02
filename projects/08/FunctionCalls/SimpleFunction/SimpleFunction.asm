// -- push local 0 --
@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// -- push local 1 --
@LCL
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// -- add --
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D

// -- not --
@SP
A=M-1
M=!M
// -- push argument 0 --
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// -- add --
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D

// -- push argument 1 --
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// -- sub --
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=D

