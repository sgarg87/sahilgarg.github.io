import numpy as np
import copy
import collections


class TrieNode:
    def __init__(self):
        self.char_nodes_map = {}
        self.is_word_end = False
        self.word = None


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root_node = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        word_len = len(word)
        curr_trie_node = self.root_node
        for curr_char_idx, curr_char in enumerate(word):
            if curr_char not in curr_trie_node.char_nodes_map:
                new_trie_node = TrieNode()
                curr_trie_node.char_nodes_map[curr_char] = new_trie_node
                del new_trie_node
            if curr_char_idx == (word_len-1):
                curr_trie_node.char_nodes_map[curr_char].is_word_end = True
                curr_trie_node.char_nodes_map[curr_char].word = word
            curr_trie_node = curr_trie_node.char_nodes_map[curr_char]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word_len = len(word)
        curr_trie_node = self.root_node
        for curr_char_idx, curr_char in enumerate(word):
            if curr_char not in curr_trie_node.char_nodes_map:
                return False
            else:
                if curr_char_idx == (word_len-1):
                    return curr_trie_node.char_nodes_map[curr_char].is_word_end
                else:
                    curr_trie_node = curr_trie_node.char_nodes_map[curr_char]

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        prefix_len = len(prefix)
        curr_trie_node = self.root_node
        for curr_char_idx, curr_char in enumerate(prefix):
            if curr_char not in curr_trie_node.char_nodes_map:
                return False
            else:
                if curr_char_idx == (prefix_len-1):
                    return True
                else:
                    curr_trie_node = curr_trie_node.char_nodes_map[curr_char]

    def return_words_with_prefix(self, prefix):
        curr_trie_node = self.root_node
        for curr_char_idx, curr_char in enumerate(prefix):
            if curr_char not in curr_trie_node.char_nodes_map:
                raise AssertionError
            curr_trie_node = curr_trie_node.char_nodes_map[curr_char]

        set_of_words_with_prefix = set()
        queue_of_trie_nodes = list()
        queue_of_trie_nodes.append(curr_trie_node)
        del curr_trie_node
        while queue_of_trie_nodes:
            curr_trie_node = queue_of_trie_nodes.pop(0)
            if curr_trie_node.is_word_end:
                assert curr_trie_node.word is not None
                set_of_words_with_prefix.add(curr_trie_node.word)
            for child_node in curr_trie_node.char_nodes_map.values():
                queue_of_trie_nodes.append(child_node)
        return set_of_words_with_prefix


class Solution(object):

    def dfs(
            self,
            board, word,
            i, j,
            visited,
            # optional, for assertions
            org_word=None
    ):
        # print('dfs({}, {})'.format(i, j))
        assert board[i, j] == word[0], 'first character not matching'
        assert (i, j) not in visited, 'already visited'
        visited.append((i, j))
        last_accessible_loc = (i, j)

        if len(word) == 1:
            # print(last_accessible_loc)
            return True, 0, last_accessible_loc, visited

        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        subword = word[1:]
        del word
        # print(org_word, subword)

        num_chars_not_found = len(subword)
        visited_from_neighbors = None
        for curr_neighbor in neighbors:
            # print('is valid neighbor')
            if not ((0 <= curr_neighbor[0] < board.shape[0]) and (0 <= curr_neighbor[1] < board.shape[1])):
                continue

            # print('is valid neighbor for proceeding search')
            if board[curr_neighbor[0], curr_neighbor[1]] != subword[0]:
                continue

            # print('is visited before')
            if curr_neighbor in visited:
                continue

            # print('curr_neighbor', curr_neighbor)

            # print('recursive call')
            is_subword_found, curr_num_chars_not_found,\
            last_accessible_loc_from_curr_neighbor_path, visited_from_curr_neighbor_path = self.dfs(
                board=board, word=subword,
                i=curr_neighbor[0], j=curr_neighbor[1],
                visited=copy.copy(visited),
                org_word=org_word,
            )
            if is_subword_found:
                # print(last_accessible_loc_from_curr_neighbor_path)
                return True, 0, last_accessible_loc_from_curr_neighbor_path, visited_from_curr_neighbor_path
            else:
                # print(curr_num_chars_not_found, visited_from_curr_neighbor_path)
                if curr_num_chars_not_found <= num_chars_not_found:
                    num_chars_not_found = curr_num_chars_not_found
                    last_accessible_loc = last_accessible_loc_from_curr_neighbor_path
                    visited_from_neighbors = visited_from_curr_neighbor_path

            del curr_num_chars_not_found, is_subword_found

        # returning the number of remaining characters which could not be found
        if visited_from_neighbors is None:
            visited_from_neighbors = visited
        # print(last_accessible_loc)
        return False, num_chars_not_found, last_accessible_loc, visited_from_neighbors

    def create_char_cell_map(self, board):
        char_cell_map = collections.defaultdict(set)
        board = np.array(board)

        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                curr_char = board[i, j]
                char_cell_map[curr_char].add((i, j))
                del curr_char

        return char_cell_map

    def search_word(self, board, word, i, j, visited=None):
        if visited is None:
            visited = list()
        is_word_found, num_chars_not_found, last_accessible_loc, visited = self.dfs(
            board=board, word=word,
            i=i, j=j,
            visited=visited,
            org_word=word,
        )
        # print(word, num_chars_not_found)
        return is_word_found, num_chars_not_found, last_accessible_loc, visited

    def trie_structure_of_words(self, words):
        trie_obj = Trie()
        for curr_word in words:
            trie_obj.insert(curr_word)

        # testing
        for curr_word in words:
            assert trie_obj.search(curr_word)

        return trie_obj

    def update_unsearchable_words(self, word_for_search, num_chars_not_found, trie_obj, words_search_map):
        assert num_chars_not_found >= 1

        words_search_map[word_for_search] = False
        curr_word_len = len(word_for_search)

        # print('---------------------')
        # print(word_for_search, num_chars_not_found)
        # searchable characters + first char of non searchable suffix
        curr_word_prefix_not_searchable = word_for_search[:curr_word_len - num_chars_not_found + 1]
        # print(curr_word_prefix_not_searchable)
        set_of_words_with_prefix_not_searchable = trie_obj.return_words_with_prefix(
            prefix=curr_word_prefix_not_searchable
        )
        # print(set_of_words_with_prefix_not_searchable)
        for curr_word_not_searchable in set_of_words_with_prefix_not_searchable:
            words_search_map[curr_word_not_searchable] = False

        return words_search_map

    def search_for_suffices_of_words_with_prefix(
            self,
            trie_obj,
            prefix_searchable_from_cell,
            board,
            last_accessible_loc,
            words_search_map,
            visited,
    ):
        print('SS................................')
        print(prefix_searchable_from_cell)
        prefix_size = len(prefix_searchable_from_cell)
        assert prefix_size == len(visited)
        assert visited[-1] == last_accessible_loc

        min_prefix_size = min(int(prefix_size/2), 4)
        for curr_prefix_size in range(prefix_size, min_prefix_size, -1):
            curr_prefix_searchable_from_cell = prefix_searchable_from_cell[:curr_prefix_size]
            visited_from_curr_prefix = visited[:curr_prefix_size]
            last_accessible_loc_from_curr_prefix = visited_from_curr_prefix[-1]

            set_of_words_with_prefix_searchable_from_cell = trie_obj.return_words_with_prefix(
                prefix=curr_prefix_searchable_from_cell
            )
            print(set_of_words_with_prefix_searchable_from_cell)

            if not set_of_words_with_prefix_searchable_from_cell:
                continue

            for curr_word_with_prefix_searchable_from_cell in set_of_words_with_prefix_searchable_from_cell:
                if curr_word_with_prefix_searchable_from_cell in words_search_map:
                    continue

                curr_suffix_to_search = \
                    curr_word_with_prefix_searchable_from_cell[curr_prefix_size-1:]
                print('curr_suffix_to_search', curr_suffix_to_search)
                # print('visited', visited)
                curr_visited = copy.copy(visited_from_curr_prefix)
                curr_visited.remove(last_accessible_loc_from_curr_prefix)
                is_suffix_searchable, _, _, _ = self.search_word(
                    board=board,
                    word=curr_suffix_to_search,
                    i=last_accessible_loc_from_curr_prefix[0],
                    j=last_accessible_loc_from_curr_prefix[1],
                    visited=curr_visited,
                )
                del curr_visited
                print(is_suffix_searchable)
                if is_suffix_searchable:
                    words_search_map[curr_word_with_prefix_searchable_from_cell] = True

        return words_search_map

    def dynamic_search(
            self,
            word_for_search,
            char_cell_map,
            board,
            words_search_map,
            trie_obj,
    ):
        word_len = len(word_for_search)

        curr_char_first_char = word_for_search[0]
        num_chars_not_found = len(word_for_search)
        last_accessible_loc = None
        visited = None
        is_word_found = False
        for curr_start_cell in char_cell_map[curr_char_first_char]:
            is_word_found_from_cell, num_chars_not_found_from_curr_cell, \
            last_accessible_loc_from_curr_cell,\
            visited_from_curr_cell = self.search_word(
                board=board, word=word_for_search,
                i=curr_start_cell[0], j=curr_start_cell[1],
            )
            # print('X', word_for_search, is_word_found_from_cell, num_chars_not_found_from_curr_cell)

            if is_word_found_from_cell:
                words_search_map[word_for_search] = True
                is_word_found = True

                curr_prefix_searchable_from_cell = word_for_search
                # print('.................')
                # print(len(word_for_search))
                # print('word_for_search', word_for_search)
                # print('curr_prefix_searchable_from_cell', curr_prefix_searchable_from_cell)
                # print('last_accessible_loc_from_curr_cell', last_accessible_loc_from_curr_cell)
                # print('visited_from_curr_cell', visited_from_curr_cell)
                words_search_map = self.search_for_suffices_of_words_with_prefix(
                    trie_obj=trie_obj,
                    prefix_searchable_from_cell=word_for_search,
                    board=board,
                    last_accessible_loc=last_accessible_loc_from_curr_cell,
                    words_search_map=words_search_map,
                    visited=visited_from_curr_cell,
                )
                del curr_prefix_searchable_from_cell

                break
            else:
                if num_chars_not_found_from_curr_cell <= num_chars_not_found:
                    num_chars_not_found = num_chars_not_found_from_curr_cell
                    last_accessible_loc = last_accessible_loc_from_curr_cell
                    visited = visited_from_curr_cell

                # curr_prefix_searchable_from_cell = word_for_search[:word_len - num_chars_not_found_from_curr_cell]
                # # print('.................')
                # # print(len(word_for_search))
                # # print('word_for_search', word_for_search)
                # # print('num_chars_not_found_from_curr_cell', num_chars_not_found_from_curr_cell)
                # # print('curr_prefix_searchable_from_cell', curr_prefix_searchable_from_cell)
                # # print('last_accessible_loc_from_curr_cell', last_accessible_loc_from_curr_cell)
                # # print('visited_from_curr_cell', visited_from_curr_cell)
                # words_search_map = self.search_for_suffices_of_words_with_prefix(
                #     trie_obj=trie_obj,
                #     prefix_searchable_from_cell=curr_prefix_searchable_from_cell,
                #     board=board,
                #     last_accessible_loc=last_accessible_loc_from_curr_cell,
                #     words_search_map=words_search_map,
                #     visited=visited_from_curr_cell,
                #     org_word_searched=word_for_search,
                # )
                # del curr_prefix_searchable_from_cell

        # if not is_word_found:
        #     words_search_map[word_for_search] = False
        #     words_search_map = self.update_unsearchable_words(
        #         word_for_search=word_for_search,
        #         num_chars_not_found=num_chars_not_found,
        #         trie_obj=trie_obj,
        #         words_search_map=words_search_map,
        #     )

        return words_search_map

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        board = np.array(board)

        trie_obj = self.trie_structure_of_words(words=words)
        char_cell_map = self.create_char_cell_map(board=board)

        words_search_map = {}
        for curr_word in words:
            if curr_word in words_search_map:
                continue

            self.dynamic_search(
                word_for_search=curr_word,
                char_cell_map=char_cell_map,
                board=board,
                words_search_map=words_search_map,
                trie_obj=trie_obj,
            )

        found_words = [x for x in words_search_map if words_search_map[x]]
        print(found_words)

        return found_words
