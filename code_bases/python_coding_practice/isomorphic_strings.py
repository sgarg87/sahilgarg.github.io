class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n != len(t):
            return False

        s_to_t_map = {}
        t_char_mapped_set = set()
        for i in range(n):
            s_char = s[i]
            t_char = t[i]

            if s_char not in s_to_t_map:
                if t_char in t_char_mapped_set:
                    return False
                s_to_t_map[s_char] = t_char
                t_char_mapped_set.add(t_char)
            else:
                if s_to_t_map[s_char] != t_char:
                    return False
        return True
