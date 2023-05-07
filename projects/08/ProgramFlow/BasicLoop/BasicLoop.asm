// -- push constant 0 --
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop local 0 --
@LCL
D=M
@0
D=D+A
@14
M=D
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

// -- label LOOP_START -- 
(LOOP_START)

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
// -- add --
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D

// -- pop local 0 --
@LCL
D=M
@0
D=D+A
@14
M=D
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

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

// -- pop argument 0 --
@ARG
D=M
@0
D=D+A
@14
M=D
@SP
M=M-1
A=M
D=M
@14
A=M
M=D

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
// -- if-goto LOOP_START --
@SP
AM=M-1
D=M
@LOOP_START
D;JNE

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
