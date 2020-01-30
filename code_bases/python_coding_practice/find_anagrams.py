import copy


class Solution(object):
    def match_anagram(self, s, n, i, char_count_map):
        while i < n:
            x = s[i]
            if x not in char_count_map:
                return False, i
            else:
                char_count_map[x] -= 1
                if char_count_map[x] == 0:
                    char_count_map.pop(x, None)
                    if not char_count_map:
                        return True, i
                i += 1

        return False, i

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        char_count_map = {}
        for x in p:
            if x not in char_count_map:
                char_count_map[x] = 0
            char_count_map[x] += 1

        print(char_count_map)

        start_indices = []
        i = 0
        curr_char_count_map = copy.copy(char_count_map)
        while i < n:
            is_match, j = self.match_anagram(s, n, i, curr_char_count_map)
            if is_match:
                start_indices.append(i)
                curr_char_count_map = copy.copy(char_count_map)
                x = s[i]
                curr_char_count_map = {}
                i = j
            else:
                i = j+1

        return start_indices
