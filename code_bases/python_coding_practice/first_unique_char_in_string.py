class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        char_count_map = {}
        for curr_char in s:
            if curr_char not in char_count_map:
                char_count_map[curr_char] = 0
            char_count_map[curr_char] += 1

        for curr_char_idx, curr_char in enumerate(s):
            if char_count_map[curr_char] == 1:
                return curr_char_idx

        return -1
