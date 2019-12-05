# Author: Kyle Schmidt
# Date: 11/26/2019
# This program contains a class named FBoard for playing a game, where player x is trying to get her piece to row 7 and
# player o is trying to make it so player x doesn't have any legal moves.


class FBoard:
    """Represents a FBoard game with data members to track the game state, the game board and where the x piece is"""
    def __init__(self):
        """Creates FBoard object"""
        self._board = [["_", "_", "_", "x", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"],
                       ["_", "_", "_", "_", "_", "_", "_", "_"], ["o", "_", "o", "_", "o", "_", "o", "_"]]
        self._game_state = "UNFINISHED"
        self._X_loc = [0, 3]

    def get_game_state(self):
        """Returns the current state of the FBoard game"""
        return self._game_state

    def move_x(self, row, column):
        """Takes a row and column and moves the x piece to that location. Returns False if the game has already been
        won, the desired space is already occupied, the move is outside the game board, or the move is not a single
        space in a diagonal direction"""

        # Check if game is already won, return False if the game is over
        if self._game_state != "UNFINISHED":
            return False

        # Check if the move is within the game board, return False if outside the game board
        if row > 7 or row < 0 or column > 7 or column < 0:
            return False

        # Check if the new location is already occupied, return False if occupied
        if self._board[row][column] != "_":
            return False

        # "x" may move one space diagonally. check to see if it is a valid move. The new row must be either be +1 or -1
        # from the current "x" location. Return False if the move is invalid.
        if row == self._X_loc[0] + 1 or row == self._X_loc[0] - 1:
            pass
        else:
            return False

        # the new column must also be either +1 or -1 from the current "x" location. Return False if the move is invalid
        if column == self._X_loc[1] + 1 or column == self._X_loc[1] - 1:
            pass
        else:
            return False

        # If all the move conditions are met: update the game board, "x" location and game status and return True.
        # The previous "x" location now becomes blank.
        self._board[self._X_loc[0]][self._X_loc[1]] = "_"

        # Place an "x" in the new spot on the board
        self._board[row][column] = "x"

        # The "x" location is updated with the new row and column
        self._X_loc = [row, column]

        # If "x" has reached row 7, the game status is updated to X_WON, otherwise the game status stays as UNFINISHED
        if row == 7:
            self._game_state = "X_WON"

        return True

    def move_o(self, from_row, from_column, to_row, to_column):
        """Takes a from row and column and a to row and column and moves the o piece to the new location. Returns False
        if the from coordinates do not hold an o piece, if the move is not allowed or the game is already won."""

        # Check if game is already won, return False if the game is over.
        if self._game_state != "UNFINISHED":
            return False

        # Check to see if the "from" location contains an "o". Return False if an "o" is not at that location.
        if self._board[from_row][from_column] != "o":
            return False

        # Check if the move is within the game board, return False if outside the game board
        if to_row > 7 or to_row < 0 or to_column > 7 or to_column < 0:
            return False

        # Check if the new location is already occupied, return False if occupied
        if self._board[to_row][to_column] != "_":
            return False

        # "o" may move one space diagonally, but the row can only decrease. Check to see if it is a valid move. The new
        # row must be -1 from the current "o" location. Return False if the move is invalid.
        if to_row != from_row - 1:
            return False

        # the new column must be either +1 or -1 from the current "o" location. Return False if the move is invalid.
        if to_column == from_column + 1 or to_column == from_column - 1:
            pass
        else:
            return False

        # If all the move conditions are met: update the game board, game status and return True.
        # The previous "o" location now becomes blank.
        self._board[from_row][from_column] = "_"

        # Place an "o" in the new spot on the board
        self._board[to_row][to_column] = "o"

        # Check if "x" has any possible moves. If "x" has no moves then "o" has won.
        # There are 4 possible moves for "x" to make (the 4 diagonals surrounding the current position).
        move_1 = [self._X_loc[0] + 1, self._X_loc[1] + 1]
        move_2 = [self._X_loc[0] + 1, self._X_loc[1] - 1]
        move_3 = [self._X_loc[0] - 1, self._X_loc[1] + 1]
        move_4 = [self._X_loc[0] - 1, self._X_loc[1] - 1]

        # check if any of the move_1 positions are outside the game board. If it is a valid board space then check if
        # the space is empty. The game continues if the space is empty.
        if 8 not in move_1 and -1 not in move_1:
            if self._board[self._X_loc[0] + 1][self._X_loc[1] + 1] == "_":
                return True

        # check if any of the move_2 positions are outside the game board. If it is a valid board space then check if
        # the space is empty. The game continues if the space is empty.
        if 8 not in move_2 and -1 not in move_2:
            if self._board[self._X_loc[0] + 1][self._X_loc[1] - 1] == "_":
                return True

        # check if any of the move_3 positions are outside the game board. If it is a valid board space then check if
        # the space is empty. The game continues if the space is empty.
        if 8 not in move_3 and -1 not in move_3:
            if self._board[self._X_loc[0] - 1][self._X_loc[1] + 1] == "_":
                return True

        # check if any of the move_4 positions are outside the game board. If it is a valid board space then check if
        # the space is empty. The game continues if the space is empty.
        if 8 not in move_4 and -1 not in move_4:
            if self._board[self._X_loc[0] - 1][self._X_loc[1] - 1] == "_":
                return True

        # If the function makes it to this point without hitting a return then "o" has won
        self._game_state = "O_WON"
        return True
