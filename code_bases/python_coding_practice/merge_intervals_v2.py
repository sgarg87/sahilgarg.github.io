import numpy as np


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals = np.array(intervals)
        assert intervals.shape[1] == 2

        # sorting on starting time
        start_times = intervals[:, 0]
        sort_idx_start_times = start_times.argsort()
        del start_times

        # linear scan to merge overlapping intervals
        non_overlapping_intervals = list()
        curr_interval = None

        for curr_interval_idx in sort_idx_start_times:

            if curr_interval is None:
                curr_interval = intervals[curr_interval_idx]
            else:
                new_interval = intervals[curr_interval_idx]

                # start time is less than end time
                if new_interval[0] <= curr_interval[1]:
                    curr_interval[1] = max(new_interval[1], curr_interval[1])
                    del new_interval
                else:
                    non_overlapping_intervals.append(curr_interval.tolist())
                    curr_interval = new_interval
                    del new_interval

        non_overlapping_intervals.append(curr_interval.tolist())

        return non_overlapping_intervals
