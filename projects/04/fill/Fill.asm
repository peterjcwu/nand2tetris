  // This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// display unit (w[0..511], h[0..255])
// 8k word 16 x 8192 + offset 16384
// screen memory map starts from 16384
// keyboard starts from 24567

    @8192
    D=A
    @n
    M=D  // n = 8k

    @RESET
    0;JMP

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @RESET
    D;JGT  // if (i-n > 0) then goto RESET

    @KBD
    D=M

    @WHITE
    D;JEQ

(BLACK)
    @addr
    A=M
    M=-1  // RAM[addr] = 0000000000000000
    @ENDIF
    0;JMP

(WHITE)
    @addr
    A=M
    M=0  // RAM[addr] = 1111111111111111

(ENDIF)
    @i
    M=M+1  // i += 1
    
    @1
    D=A
    @addr
    M=D+M  // addr += 1

    @LOOP
    0;JMP  // goto LOOP
   
(RESET)
    @SCREEN
    D=A
    @addr
    M=D  // addr = 16384

    @i
    M=0  // i = 0

    @LOOP
    0;JMP  // goto LOOP
