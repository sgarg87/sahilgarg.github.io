import numpy as np
import copy
import collections


class Solution(object):

    def dfs(self, board, word, i, j, visited):
        assert board[i, j] == word[0]
        assert (i, j) not in visited
        visited.add((i, j))

        if len(word) == 1:
            return True

        neighbors = [
            (i-1, j), (i+1, j),
            (i, j-1), (i, j+1),
        ]

        subword = word[1:]
        for curr_neighbor in neighbors:
            if not ((0 <= curr_neighbor[0] < board.shape[0]) and (0 <= curr_neighbor[1] < board.shape[1])):
                continue

            if board[curr_neighbor[0], curr_neighbor[1]] != word[1]:
                continue

            if curr_neighbor in visited:
                continue

            is_subword_found = self.dfs(
                board=board, word=subword,
                i=curr_neighbor[0], j=curr_neighbor[1],
                visited=copy.copy(visited),
            )
            if is_subword_found:
                return True

        return False

    def search_word(self, board, word, i, j):
        visited = set()
        is_word_found = self.dfs(board=board, word=word, i=i, j=j, visited=visited)
        return is_word_found

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        char_cell_map = collections.defaultdict(list)
        board = np.array(board)
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                curr_char = board[i, j]
                char_cell_map[curr_char].append((i, j))
                del curr_char

        found_words = []
        for curr_word in words:
            curr_char_first_char = curr_word[0]
            for curr_start_cell in char_cell_map[curr_char_first_char]:
                is_word_found = self.search_word(
                    board=board, word=curr_word,
                    i=curr_start_cell[0], j=curr_start_cell[1],
                )
                if is_word_found:
                    found_words.append(curr_word)
                    break

        return found_words
