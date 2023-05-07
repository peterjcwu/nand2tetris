// -- bootstrap --
@261
D=A
@SP
M=D

// -- function Sys.init 0 --
(Sys.init)

// -- push constant 4 --
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- call Main.fibonacci 1 --
@Main.fibonacci$ret.13
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.13)

// -- label WHILE -- 
(WHILE)

// -- goto WHILE --
@WHILE
0;JMP
// -- function Main.fibonacci 0 --
(Main.fibonacci)

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
// -- push constant 2 --
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- less than -- 
@SP
AM=M-1
D=M
A=A-1
D=M-D
@lt.pass.0018
D;JLT
@SP
A=M-1
M=0
@lt.after.0019
0;JMP
(lt.pass.0018)
@SP
A=M-1
M=-1
(lt.after.0019)

// -- if-goto IF_TRUE --
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE

// -- goto IF_FALSE --
@IF_FALSE
0;JMP
// -- label IF_TRUE -- 
(IF_TRUE)

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
// -- label IF_FALSE -- 
(IF_FALSE)

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
// -- push constant 2 --
@2
D=A
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

// -- call Main.fibonacci 1 --
@Main.fibonacci$ret.24
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.24)

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
// -- push constant 1 --
@1
D=A
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

// -- call Main.fibonacci 1 --
@Main.fibonacci$ret.28
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.28)

// -- add --
@SP
AM=M-1
D=M
A=A-1
D=D+M
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
