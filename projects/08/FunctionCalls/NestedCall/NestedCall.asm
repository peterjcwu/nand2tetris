// -- function Sys.init 0 --
(Sys.init)

// -- push constant 4000 --
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop pointer 0 --
@3
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

// -- push constant 5000 --
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop pointer 1 --
@4
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

// -- call Sys.main 0 --
@Sys.main$ret.13
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
@Sys.main
0;JMP
(Sys.main$ret.13)

// -- pop temp 1 --
@6
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

// -- label LOOP -- 
(LOOP)

// -- goto LOOP --
@LOOP
0;JMP
// -- function Sys.main 5 --
(Sys.main)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1

// -- push constant 4001 --
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop pointer 0 --
@3
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

// -- push constant 5001 --
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop pointer 1 --
@4
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

// -- push constant 200 --
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop local 1 --
@LCL
D=M
@1
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

// -- push constant 40 --
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop local 2 --
@LCL
D=M
@2
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

// -- push constant 6 --
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop local 3 --
@LCL
D=M
@3
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

// -- push constant 123 --
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- call Sys.add12 1 --
@Sys.add12$ret.38
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
@Sys.add12
0;JMP
(Sys.add12$ret.38)

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
// -- push local 2 --
@LCL
D=M
@2
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// -- push local 3 --
@LCL
D=M
@3
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// -- push local 4 --
@LCL
D=M
@4
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

// -- add --
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D

// -- add --
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D

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
// -- function Sys.add12 0 --
(Sys.add12)

// -- push constant 4002 --
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop pointer 0 --
@3
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

// -- push constant 5002 --
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- pop pointer 1 --
@4
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
// -- push constant 12 --
@12
D=A
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
