// -- init --
@256
D=A
@SP
M=D
// -- push constant 10 --
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop local 0 -- 
@0
D=A
@LCL
D=D+M
@14
M=D
@SP
AM=M-1
D=M
@14
A=M
M=D
// -- push constant 21 --
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 22 --
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop argument 2 -- 
@2
D=A
@ARG
D=D+M
@14
M=D
@SP
AM=M-1
D=M
@14
A=M
M=D
// -- pop argument 1 -- 
@1
D=A
@ARG
D=D+M
@14
M=D
@SP
AM=M-1
D=M
@14
A=M
M=D
// -- push constant 36 --
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop this 6 -- 
@6
D=A
@THIS
D=D+M
@14
M=D
@SP
AM=M-1
D=M
@14
A=M
M=D
// -- push constant 42 --
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 45 --
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop that 5 -- 
@5
D=A
@THAT
D=D+M
@14
M=D
@SP
AM=M-1
D=M
@14
A=M
M=D
// -- pop that 2 -- 
@2
D=A
@THAT
D=D+M
@14
M=D
@SP
AM=M-1
D=M
@14
A=M
M=D
// -- push constant 510 --
@510
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop temp 6 -- 
@11
D=A
@14
M=D
@SP
AM=M-1
D=M
@14
A=M
M=D
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
// -- push that 5 --
@THAT
D=M
@5
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
@SP
AM=M-1
D=D+M
M=D
@SP
M=M+1

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
@SP
AM=M-1
D=M-D
M=D
@SP
M=M+1

// -- push this 6 --
@THIS
D=M
@6
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// -- push this 6 --
@THIS
D=M
@6
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
@SP
AM=M-1
D=D+M
M=D
@SP
M=M+1

// -- sub --
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
M=D
@SP
M=M+1

// -- push temp 6 --
@11
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
@SP
AM=M-1
D=D+M
M=D
@SP
M=M+1

