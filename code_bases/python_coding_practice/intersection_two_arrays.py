

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        char_count_map = {}
        for char in nums1:
            if char not in char_count_map:
                char_count_map[char] = 0
            char_count_map[char] += 1

        output_nums = []
        for char in nums2:
            if char in char_count_map:
                if char_count_map[char] > 0:
                    char_count_map[char] -= 1
                    output_nums.append(char)

        return output_nums
