// -- bootstrap --
@261
D=A
@SP
M=D

// -- function Sys.init 0 --
(Sys.init)

// -- push constant 6 --
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 8 --
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- call Class1.set 2 --
@Class1.set$ret.11
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@7
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Class1.set$ret.11)

// -- pop temp 0 --
@5
D=A
@14
M=D
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// -- push constant 23 --
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 15 --
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- call Class2.set 2 --
@Class2.set$ret.15
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@7
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Class2.set$ret.15)

// -- pop temp 0 --
@5
D=A
@14
M=D
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// -- call Class1.get 0 --
@Class1.get$ret.17
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(Class1.get$ret.17)

// -- call Class2.get 0 --
@Class2.get$ret.18
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(Class2.get$ret.18)

// -- label WHILE -- 
(WHILE)

// -- goto WHILE --
@WHILE
0;JMP
// -- function Class1.set 0 --
(Class1.set)

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
// -- pop static 0 --
@SP
M=M-1
A=M
D=M
@Class1.0
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
// -- pop static 1 --
@SP
M=M-1
A=M
D=M
@Class1.1
M=D

// -- push constant 0 --
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- return --
@LCL
D=M
@R13
M=D
@R13
D=M
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
@R14
A=M
0;JMP
// -- function Class1.get 0 --
(Class1.get)

// -- push static 0 --
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// -- push static 1 --
@Class1.1
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

// -- return --
@LCL
D=M
@R13
M=D
@R13
D=M
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
@R14
A=M
0;JMP
// -- function Class2.set 0 --
(Class2.set)

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
// -- pop static 0 --
@SP
M=M-1
A=M
D=M
@Class2.0
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
// -- pop static 1 --
@SP
M=M-1
A=M
D=M
@Class2.1
M=D

// -- push constant 0 --
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- return --
@LCL
D=M
@R13
M=D
@R13
D=M
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
@R14
A=M
0;JMP
// -- function Class2.get 0 --
(Class2.get)

// -- push static 0 --
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// -- push static 1 --
@Class2.1
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

// -- return --
@LCL
D=M
@R13
M=D
@R13
D=M
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
@R14
A=M
0;JMP
