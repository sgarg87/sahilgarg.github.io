class Solution(object):
    def longest_palindrome(self, s, left_idx, right_idx, string_len):
        if ((left_idx > 0) and (right_idx < (string_len-1))) and (s[left_idx-1] == s[right_idx+1]):
            return self.longest_palindrome(
                s=s,
                left_idx=left_idx-1,
                right_idx=right_idx+1,
                string_len=string_len,
            )
        else:
            return right_idx-left_idx+1, s[left_idx:right_idx+1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string_len = len(s)

        if not s:
            return ''

        max_len_palindrome = 1
        max_str_palindrome = s[0]
        for curr_idx in range(string_len):
            curr_palindrome_len, curr_palindrome = self.longest_palindrome(
                s=s, left_idx=curr_idx, right_idx=curr_idx, string_len=string_len,
            )
            if curr_palindrome_len >= max_len_palindrome:
                max_len_palindrome = curr_palindrome_len
                max_str_palindrome = curr_palindrome

        for curr_idx in range(string_len-1):
            if s[curr_idx] == s[curr_idx+1]:
                curr_palindrome_len, curr_palindrome = self.longest_palindrome(
                    s=s, left_idx=curr_idx, right_idx=curr_idx+1, string_len=string_len,
                )
                if curr_palindrome_len >= max_len_palindrome:
                    max_len_palindrome = curr_palindrome_len
                    max_str_palindrome = curr_palindrome

        return max_str_palindrome
