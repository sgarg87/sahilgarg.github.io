class Solution(object):
    def palindrome_recursive(self, s, i, j, del_count):
        if i >= j:
            return True
        # print(i, j, del_count)

        if s[i] == s[j]:
            return self.palindrome_recursive(
                s=s, i=i+1, j=j-1, del_count=del_count,
            )
        else:
            if del_count >= 1:
                return False
            else:
                del_count += 1
                left_char_del = self.palindrome_recursive(
                    s=s, i=i+1, j=j, del_count=del_count,
                )
                right_char_del = self.palindrome_recursive(
                    s=s, i=i, j=j-1, del_count=del_count,
                )
                return left_char_del or right_char_del

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        return self.palindrome_recursive(s=s, i=0, j=n-1, del_count=0)
