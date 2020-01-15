import numpy as np


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.board = np.zeros((n, n), dtype=np.int)

        # positive count for player 1
        # negative count for player 2
        self.row_count_map = {}
        self.col_count_map = {}
        self.diag_map = {}

    def _get_move_type(self, player):
        if player == 1:
            move_type = -1
        elif player == 2:
            move_type = 1
        else:
            raise AssertionError
        return move_type

    def get_diag_types(self, row, col):
        row_col_sum = row+col+1

        if (row_col_sum == self.n) and (row == col):
            return [-1, 1]
        elif row_col_sum == self.n:
            return [-1]
        elif row == col:
            return [1]
        else:
            return []

    def _move_along_diag(self, row, col, move_type):
        diag_types = self.get_diag_types(row=row, col=col)

        for curr_diag_type in diag_types:
            if curr_diag_type not in self.diag_map:
                self.diag_map[curr_diag_type] = move_type
            else:
                # already invalidated
                if self.diag_map[curr_diag_type] is None:
                    continue
                else:
                    # another player crosses the diagonal
                    if (self.diag_map[curr_diag_type]*move_type) < 0:
                        self.diag_map[curr_diag_type] = None
                    else:
                        self.diag_map[curr_diag_type] += move_type

                        if self.diag_map[curr_diag_type] == (move_type*self.n):
                            return True
        return False

    def _move_along_row(self, row, move_type):
        if row not in self.row_count_map:
            self.row_count_map[row] = move_type
        else:
            # already invalidated
            if self.row_count_map[row] is None:
                return False
            else:
                # another player crosses the row
                if (self.row_count_map[row]*move_type) < 0:
                    self.row_count_map[row] = None
                else:
                    self.row_count_map[row] += move_type

                    if self.row_count_map[row] == (move_type*self.n):
                        return True
        return False

    def _move_along_col(self, col, move_type):
        if col not in self.col_count_map:
            self.col_count_map[col] = move_type
        else:
            # already invalidated
            if self.col_count_map[col] is None:
                return False
            else:
                # another player crosses the column
                if (self.col_count_map[col] * move_type) < 0:
                    self.col_count_map[col] = None
                else:
                    self.col_count_map[col] += move_type

                    if self.col_count_map[col] == (move_type*self.n):
                        return True
        return False

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        assert self.board[row, col] == 0
        self.board[row, col] = player

        move_type = self._get_move_type(player=player)

        is_win = self._move_along_row(row=row, move_type=move_type)
        if is_win:
            return player

        is_win = self._move_along_col(col=col, move_type=move_type)
        if is_win:
            return player

        is_win = self._move_along_diag(row=row, col=col, move_type=move_type)
        if is_win:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
