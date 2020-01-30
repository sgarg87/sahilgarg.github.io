class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        m = len(s)
        n = len(t)
        if m > n:
            return False

        i = 0
        for j, x in enumerate(t):
            if (n-j) < (m-i):
                return False

            if x == s[i]:
                i += 1
                if i == m:
                    return True
        return False
