// -- init --
@256
D=A
@SP
M=D
// -- push constant 17 --
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 17 --
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- eq -- 
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@eq.pass.0000
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@eq.after.0001
0;JMP
(eq.pass.0000)
@SP
A=M
M=-1
@SP
M=M+1
(eq.after.0001)

// -- push constant 17 --
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 16 --
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- eq -- 
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@eq.pass.0002
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@eq.after.0003
0;JMP
(eq.pass.0002)
@SP
A=M
M=-1
@SP
M=M+1
(eq.after.0003)

// -- push constant 16 --
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 17 --
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- eq -- 
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@eq.pass.0004
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@eq.after.0005
0;JMP
(eq.pass.0004)
@SP
A=M
M=-1
@SP
M=M+1
(eq.after.0005)

// -- push constant 892 --
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 891 --
@891
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
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@lt.pass.0006
D;JLT
@SP
A=M
M=0
@SP
M=M+1
@lt.after.0007
0;JMP
(lt.pass.0006)
@SP
A=M
M=-1
@SP
M=M+1
(lt.after.0007)

// -- push constant 891 --
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 892 --
@892
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
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@lt.pass.0008
D;JLT
@SP
A=M
M=0
@SP
M=M+1
@lt.after.0009
0;JMP
(lt.pass.0008)
@SP
A=M
M=-1
@SP
M=M+1
(lt.after.0009)

// -- push constant 891 --
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 891 --
@891
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
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@lt.pass.0010
D;JLT
@SP
A=M
M=0
@SP
M=M+1
@lt.after.0011
0;JMP
(lt.pass.0010)
@SP
A=M
M=-1
@SP
M=M+1
(lt.after.0011)

// -- push constant 32767 --
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 32766 --
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- greater than -- 
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@gt.pass.0012
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@gt.after.0013
0;JMP
(gt.pass.0012)
@SP
A=M
M=-1
@SP
M=M+1
(gt.after.0013)

// -- push constant 32766 --
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 32767 --
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- greater than -- 
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@gt.pass.0014
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@gt.after.0015
0;JMP
(gt.pass.0014)
@SP
A=M
M=-1
@SP
M=M+1
(gt.after.0015)

// -- push constant 32766 --
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 32766 --
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- greater than -- 
@SP
AM=M-1
D=M
@13
M=D
@SP
AM=M-1
D=M
@13
D=D-M
@gt.pass.0016
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@gt.after.0017
0;JMP
(gt.pass.0016)
@SP
A=M
M=-1
@SP
M=M+1
(gt.after.0017)

// -- push constant 57 --
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 31 --
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- push constant 53 --
@53
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
@SP
AM=M-1
D=D+M
M=D
@SP
M=M+1

// -- push constant 112 --
@112
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
@SP
AM=M-1
D=M-D
M=D
@SP
M=M+1

// -- and --
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D&M
M=D
@SP
M=M+1
// -- push constant 82 --
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// -- or --
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D|M
M=D
@SP
M=M+1
// -- not --
@SP
AM=M-1
M=!M
@SP
M=M+1
