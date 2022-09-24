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
// TODO: the screen var is redundant
(LOOP)
    @KBD
    D = M
    @SETBLACK
    D;JGT
    @color 
    M = 0 // 0 is white and -1 is black

    @FILL
    0;JMP

    (SETBLACK)
    @color
    M = -1
    
    (FILL)
        @SCREEN
        D = A
        @screen // variable holding the current screen mem location
        M = D 

        // NUMROWS = 256
        @256
        D = A
        @NUMROWS
        M = D 

        // NUMCOLS = 32
        @32
        D = A
        @NUMCOLS
        M = D

        // for(row=0; row<256;row++):
        @row
        M = 0
        (ROWLOOP)
            // row < 256
            @row
            D = M
            @NUMROWS 
            D = M - D // 256 - row 
            @LOOP
            D;JEQ
            // body:
                // for(col=0; col<32; col++):
                @col
                M = 0
                (COLLOOP)
                    // col < 32
                    @col
                    D = M
                    @NUMCOLS
                    D = M - D // 32 - col
                    @ROWITER
                    D;JEQ
                        // body:
                        @color
                        D = M
                        @screen
                        A = M // M = Ram[screen]
                        M = D // Ram[screen] = D/color  -> set the current word to black or white
                        @screen 
                        M = M+1 // screen + 16 -> next word
                    // col++
                    @col
                    M = M+1
                @COLLOOP
                0;JMP
            // row++
            (ROWITER)
            @row
            M = M+1
        @ROWLOOP
        0;JMP
@LOOP
0;JMP

