import heapq


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top_three_heap = list()

        max_num = nums[0]
        for x in nums:
            max_num = max(max_num, x)

            if x in top_three_heap:
                continue

            if len(top_three_heap) < 3:
                heapq.heappush(top_three_heap, x)
            else:
                if x <= top_three_heap[0]:
                    continue
                else:
                    assert x > top_three_heap[0]
                    heapq.heappop(top_three_heap)
                    heapq.heappush(top_three_heap, x)

        print(top_three_heap)
        if len(top_three_heap) < 3:
            return max_num
        else:
            return top_three_heap[0]
