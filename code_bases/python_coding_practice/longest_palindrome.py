class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        char_count_map = {}
        for curr_char in s:
            if curr_char not in char_count_map:
                char_count_map[curr_char] = 0
            char_count_map[curr_char] += 1

        palindrome_len = 0
        is_odd_count_observed = False
        for curr_char in char_count_map:
            curr_count = char_count_map[curr_char]
            if (curr_count % 2) == 0:
                palindrome_len += curr_count
            else:
                is_odd_count_observed = True
                if curr_count >= 3:
                    palindrome_len += (curr_count-1)

        if is_odd_count_observed:
            palindrome_len += 1

        return palindrome_len
