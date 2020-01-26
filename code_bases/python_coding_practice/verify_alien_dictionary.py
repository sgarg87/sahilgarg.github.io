class Solution(object):
    def _init_alphabet_order(self, order):
        char_idx_map = {}
        for i, char in enumerate(order):
            assert char not in char_idx_map
            char_idx_map[char] = i
        self.char_idx_map = char_idx_map

    def is_pair_ordered(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        min_n = min(n1, n2)

        for i in range(min_n):
            idx1 = self.char_idx_map[word1[i]]
            idx2 = self.char_idx_map[word2[i]]

            if idx1 < idx2:
                return True
            elif idx1 > idx2:
                return False
            else:
                continue

        if n1 <= n2:
            return True
        else:
            return False

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        self._init_alphabet_order(order=order)

        num_words = len(words)
        for curr_idx in range(num_words-1):
            is_ordered_pair = self.is_pair_ordered(word1=words[curr_idx], word2=words[curr_idx+1])

            if not is_ordered_pair:
                return False

        return True
