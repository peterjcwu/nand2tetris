// Program: Rectangle.asm
// Draws a filled rectangle at the screens's top left corner.
// The rectangle's width is 16 pixels, and its height is RAM[0]
// Usage: put a non-negative number (rectangle's height) in RAM[0]

    @R0
    D=M
    @n
    M=D  // n = R0

    @i
    M=0  // i = 0

    @SCREEN
    D=A
    @addr
    M=D  // addr = 16384

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @END
    D;JGT  // if (i-n > 0) then goto END

    @addr
    A=M
    M=-1  // RAM[addr] = 1111111111111111

    @i
    M=M+1  // i += 1
    
    @32
    D=A
    @addr
    M=D+M  // addr += 32
    @LOOP
    0;JMP  // goto LOOP

(END)
    @END
    0;JMP
