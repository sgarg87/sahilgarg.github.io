import heapq


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True

        heapq.heapify(intervals)
        curr_interval = heapq.heappop(intervals)

        while intervals:
            if curr_interval[1] > intervals[0][0]:
                return False
            else:
                curr_interval = heapq.heappop(intervals)

        return True
