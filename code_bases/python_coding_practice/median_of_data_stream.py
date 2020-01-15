import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._left_heap = list()
        self._right_heap = list()
        self._median_nums = []
        self._num_elements = 0

    def _pop_max_from_left_heap(self) -> None:
        assert self._left_heap
        heapq.heappop(self._left_heap)

    def _pop_min_from_right_heap(self) -> None:
        assert self._right_heap
        heapq.heappop(self._right_heap)

    def _peek_max_from_left_heap(self) -> int:
        assert self._left_heap
        return self._left_heap[0][1]

    def _peek_min_from_right_heap(self) -> int:
        assert self._right_heap
        return self._right_heap[0][1]

    def _push_to_left_heap(self, num: int) -> None:
        heapq.heappush(self._left_heap, (-num, num))

    def _push_to_right_heap(self, num: int) -> None:
        heapq.heappush(self._right_heap, (num, num))

    def adjust_median(self, num):
        len_median_nums = len(self._median_nums)
        if len_median_nums <= 1:
            self._median_nums.append(num)
            self._median_nums.sort()
        else:
            assert len_median_nums == 2
            if num <= self._median_nums[0]:
                self._push_to_left_heap(num=num)
                self._push_to_right_heap(num=self._median_nums[1])
                self._median_nums = self._median_nums[0:1]
            elif num >= self._median_nums[1]:
                self._push_to_left_heap(num=self._median_nums[0])
                self._push_to_right_heap(num=num)
                self._median_nums = self._median_nums[1:]
            else:
                assert self._median_nums[0] <= num <= self._median_nums[1]
                self._push_to_left_heap(num=self._median_nums[0])
                self._push_to_right_heap(num=self._median_nums[1])
                self._median_nums = [num]

    def addNum(self, num: int) -> None:
        # less than two elements added
        if self._num_elements <= 2:
            assert not self._left_heap
            assert not self._right_heap
            self.adjust_median(num=num)
        else:
            assert self._left_heap
            assert self._right_heap

            max_left_heap = self._peek_max_from_left_heap()
            min_right_heap = self._peek_min_from_right_heap()
            if num < max_left_heap:
                self._pop_max_from_left_heap()
                self._push_to_left_heap(num=num)
                self.adjust_median(num=max_left_heap)
            elif num > min_right_heap:
                self._pop_min_from_right_heap()
                self._push_to_right_heap(num=num)
                self.adjust_median(num=min_right_heap)
            else:
                self.adjust_median(num=num)

        self._num_elements += 1

    def findMedian(self) -> float:
        assert self._median_nums
        return float(sum(self._median_nums)) / len(self._median_nums)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
