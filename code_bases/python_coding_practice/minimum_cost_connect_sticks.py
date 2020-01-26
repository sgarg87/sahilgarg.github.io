import heapq


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)

        cost = 0
        while sticks:
            min_len_stick = heapq.heappop(sticks)
            if not sticks:
                return cost
            else:
                sec_min_stick = heapq.heappop(sticks)
                new_len = min_len_stick+sec_min_stick
                heapq.heappush(sticks, new_len)
                cost += new_len

        return cost
