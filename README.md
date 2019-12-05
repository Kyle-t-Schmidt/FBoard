# FBoard

## Introduction
This was the final project for my introduction to computer science class. While not complex, I demonstate several programming methods including:
* Comparison and logical operators
* Creating classes and functions
* String manipulation and lists
* Loops

## Program Purpose
The program contains a class named FBoard for playing a game, where player "x" is trying to get thier piece to the bottom row of the game board and player "o" is trying to make it so player "x" doesn't have any legal moves. The gameplay is as follows:
* The board is 8x8
* The starting position of the "x" piece is the top row, 4 spaces from the left (index 0,3)
* The starting position of the "o" pieces is every other space on the bottom row (index 7,0; 7,2; 7,4 and 7,6)
* "x" piece may move diagonally either forward or backward.
* "o" pieces also move diagonally but may only move forward (toward the top row).
* Pieces may not move to already occupied spaces or off the game board.

## Using the program
Create an object of class Fboard. The Fboard class takes no arguments and initilaizes with the "x" and "o" pieces at the correct starting positions as outlined above. The game state initializes as "UNFINISHED".

"x" and "o" players take turns moving their pieces using the move_x and move_o functions of the Fboard class.

move_x takes a row and a column and moves the "x" piece to that location. False will be returned if the game has already ended or the move is not allowed per the game rules. True will be returned if the move is successful.

move_o takes a from-row, a from-column, a to-row and a to-column and moves the "o" piece to the new location. False will be returned if the game has already ended or the move is not allowed per the game rules. True will be returned if the move is successful.

players can check the game status using the get_game_state function of the Fboard class. The game state will return one of three game states: "X_WON", "O_WON" or "UNFINISHED".
