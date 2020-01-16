class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_count_map = {}
        for curr_char in s:
            if curr_char not in char_count_map:
                char_count_map[curr_char] = 0
            char_count_map[curr_char] += 1

        if len(s)%2 == 1:
            is_odd_len_str = True
        else:
            is_odd_len_str = False

        num_odd_count_chars = 0
        for curr_count in char_count_map.values():
            if (curr_count % 2) == 1:
                if not is_odd_len_str:
                    return False
                else:
                    num_odd_count_chars += 1
                    if num_odd_count_chars > 1:
                        return False

        return True


