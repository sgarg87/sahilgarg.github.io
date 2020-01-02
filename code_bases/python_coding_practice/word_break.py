class Solution(object):
    def _init_word_dict(self, wordDict):
        self.wordDict = wordDict
        min_word_len = 1e100
        for curr_word in self.wordDict:
            min_word_len = min(min_word_len, len(curr_word))
        self.min_word_len = min_word_len
        self.word_breakable_map = {}

    def _is_word_breakble(self, s, len_s):
        if s in self.word_breakable_map:
            return self.word_breakable_map[s]

        if not s:
            is_breakable = True
        elif len_s < self.min_word_len:
            return False
        elif s in self.wordDict:
            is_breakable = True
        else:
            is_breakable = self._word_break(s=s, len_s=len_s)

        self.word_breakable_map[s] = is_breakable

        return is_breakable

    def _word_break(self, s, len_s):
        if s in self.wordDict:
            return True

        is_breakable = False
        for i in range(1, len_s):
            is_left_breakable = self._is_word_breakble(s=s[:i], len_s=i)
            is_right_breakable = self._is_word_breakble(s=s[i:], len_s=(len_s-i))
            if is_left_breakable and is_right_breakable:
                is_breakable = True
                break
        return is_breakable

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self._init_word_dict(wordDict=wordDict)
        if not s:
            return False

        return self._word_break(s=s, len_s=len(s))
