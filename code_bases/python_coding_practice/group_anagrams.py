import collections
# import heapq


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = collections.defaultdict(list)
        for curr_str in strs:
            curr_key = ''.join(sorted(curr_str))
            anagrams_map[curr_key].append(curr_str)

        return anagrams_map.values()
