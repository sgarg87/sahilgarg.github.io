class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        if not haystack:
            return -1

        len_haystack = len(haystack)
        len_needle = len(needle)

        haystack_idx = 0
        needle_idx = 0
        curr_idx = 0

        while haystack_idx < len_haystack:
            if haystack[curr_idx] == needle[needle_idx]:
                curr_idx += 1
                needle_idx += 1

                # match completed
                if needle_idx == len_needle:
                    return haystack_idx

                # order matters of if conditions matters here
                # match not completed
                if curr_idx == len_haystack:
                    return -1
            else:
                haystack_idx += 1
                curr_idx = haystack_idx
                needle_idx = 0

        return -1
