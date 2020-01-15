class Solution(object):

    def compute_char_counts_map(self, str):
        counts_map = {}
        for curr_char in str:
            if curr_char not in counts_map:
                counts_map[curr_char] = 0
            counts_map[curr_char] += 1
        return counts_map

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counts_map = self.compute_char_counts_map(str=s)
        t_counts_map = self.compute_char_counts_map(str=t)

        if len(s_counts_map.keys()) != len(t_counts_map.keys()):
            return False

        for curr_char in s_counts_map:
            if curr_char not in t_counts_map:
                return False
            else:
                if t_counts_map[curr_char] != s_counts_map[curr_char]:
                    return False
        return True
