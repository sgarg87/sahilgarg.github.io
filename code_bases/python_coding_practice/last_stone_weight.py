import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while stones:
            max_weight_stone = heapq.heappop(stones)
            max_weight_stone *= -1

            if not stones:
                return max_weight_stone
            else:
                second_max_weight_stone = heapq.heappop(stones)
                second_max_weight_stone *= -1
                weight_diff = max_weight_stone-second_max_weight_stone
                if weight_diff != 0:
                    heapq.heappush(stones, -weight_diff)
                else:
                    pass
        return 0

