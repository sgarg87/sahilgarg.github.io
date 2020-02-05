import collections


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_count = collections.Counter(nums)

        out = set()
        for x in nums_count:
            # print(x)
            for y in nums_count:
                if (x == y) and nums_count[x] < 2:
                    continue

                rem = -x-y
                # print(x, y, rem)
                if rem not in nums_count:
                    continue
                else:
                    if (rem == x) or (rem == y):
                        if (x == y) and (nums_count[rem] < 3):
                            continue
                        elif nums_count[rem] < 2:
                            continue

                    out.add(tuple(sorted([x, y, rem])))

        out = [list(x) for x in out]

        return out
