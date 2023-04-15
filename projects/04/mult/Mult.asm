// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// Pseudo code:
//     i = 1
//     sum = 0
// LOOP:
//     if i > RAM[1] goto STOP
//     sum += RAM[0]
//     i += 1
//     goto LOOP
// STOP:

    @i
    M=1  // i = 1

    @sum
    M=0  // sum = 0

(LOOP)
    @i
    D=M
    @R1
    D=D-M
    @STOP
    D;JGT  // if i-R1 > 0 goto STOP
    
    @R0
    D=M
    @sum
    M=M+D  // sum += R0

    @i
    M=M+1  // i += 1
    
    @LOOP
    0;JMP

(STOP)
    @sum
    D=M
    @R2
    M=D  // RAM[2] = sum    

(END)
    @END
    0;JMP
