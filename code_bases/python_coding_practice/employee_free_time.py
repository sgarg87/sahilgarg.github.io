import heapq


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        if not schedule:
            return []

        start_times_heap = []
        for curr_emp in schedule:
            for curr_interval_obj in curr_emp:
                # print(curr_interval_obj.start, curr_interval_obj.end)
                start_times_heap.append((curr_interval_obj.start, curr_interval_obj.end))
                del curr_interval_obj
            del curr_emp
        heapq.heapify(start_times_heap)

        curr_time = start_times_heap[0][0]

        free_intervals = list()
        while start_times_heap:
            start, end = heapq.heappop(start_times_heap)
            print(curr_time, start, end)
            if curr_time < start:
                curr_free_interval = Interval(start=curr_time, end=start)
                free_intervals.append(curr_free_interval)

            if end > curr_time:
                curr_time = end

        return free_intervals
