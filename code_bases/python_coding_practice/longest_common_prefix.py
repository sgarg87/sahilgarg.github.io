class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        len_strs = [len(x) for x in strs]
        min_len_strs = min(len_strs)
        prefix = ''

        for curr_idx in range(min_len_strs):
            curr_char = strs[0][curr_idx]
            for curr_str in strs:
                if curr_str[curr_idx] != curr_char:
                    return prefix
            prefix += curr_char

        return prefix

