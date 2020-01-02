import numpy as np


class Node:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class Heap:
    # min heap by default
    def __init__(self, max_size=1000):
        self.max_size = max_size
        self.nodes_arr = -1 * np.ones(max_size, dtype=np.object)
        self.last_idx = -1

    def _parent_idx(self, child_idx):
        child_idx_mod_2 = (child_idx % 2)
        if child_idx_mod_2 == 1:
            parent_idx = int(child_idx / 2)
        elif child_idx_mod_2 == 0:
            parent_idx = int((child_idx-1)/2)
        else:
            raise AssertionError('invalid mod func value')
        return parent_idx

    def insert(self, node):
        # added element as tbe last leaf
        self.last_idx += 1
        self.nodes_arr[self.last_idx] = node

        child_idx = self.last_idx
        while child_idx != 0:
            parent_idx = self._parent_idx(child_idx=child_idx)

            # swap parent and child
            if self.nodes_arr[child_idx].end_time < self.nodes_arr[parent_idx].end_time:
                parent_temp = self.nodes_arr[parent_idx]
                self.nodes_arr[parent_idx] = self.nodes_arr[child_idx]
                self.nodes_arr[child_idx] = parent_temp
                del parent_temp
                child_idx = parent_idx
            else:
                break

    def peek_min(self):
        if self.last_idx >= 0:
            return self.nodes_arr[0]
        else:
            assert self.last_idx == -1
            return None

    def _left_child_idx(self, parent_idx):
        left_child_idx = (parent_idx*2)+1
        if left_child_idx > self.last_idx:
            return None
        else:
            return left_child_idx

    def _right_child_idx(self, parent_idx):
        right_child_idx = (parent_idx*2)+2
        if right_child_idx > self.last_idx:
            return None
        else:
            return right_child_idx

    def pop_min(self):

        if self.last_idx >= 0:
            min_node = self.nodes_arr[0]

            # last leaf value becomes root node
            self.nodes_arr[0] = self.nodes_arr[self.last_idx]
            self.last_idx -= 1

            parent_idx = 0
            while parent_idx < self.last_idx:
                left_child_idx = self._left_child_idx(parent_idx=parent_idx)
                right_child_idx = self._right_child_idx(parent_idx=parent_idx)

                is_parent_greater_than_left_else_right_child = None
                parent_val = self.nodes_arr[parent_idx].end_time

                if (left_child_idx is not None) and (self.nodes_arr[left_child_idx].end_time < parent_val):
                    is_parent_greater_than_left_else_right_child = True

                if (right_child_idx is not None) and (self.nodes_arr[right_child_idx].end_time < parent_val):
                    if left_child_idx is None:
                        is_parent_greater_than_left_else_right_child = False
                    else:
                        if self.nodes_arr[right_child_idx].end_time < self.nodes_arr[left_child_idx].end_time:
                            is_parent_greater_than_left_else_right_child = False

                if is_parent_greater_than_left_else_right_child is None:
                    break
                else:
                    parent_temp = self.nodes_arr[parent_idx]
                    if is_parent_greater_than_left_else_right_child:
                        self.nodes_arr[parent_idx] = self.nodes_arr[left_child_idx]
                        self.nodes_arr[left_child_idx] = parent_temp
                        parent_idx = left_child_idx
                    else:
                        self.nodes_arr[parent_idx] = self.nodes_arr[right_child_idx]
                        self.nodes_arr[right_child_idx] = parent_temp
                        parent_idx = right_child_idx
                    del parent_temp
            return min_node
        else:
            assert self.last_idx == -1
            raise AssertionError

    def num_elements_in_heap(self):
        return self.last_idx+1


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals = np.array(intervals)
        assert intervals.shape[1] == 2

        # sorting on starting time
        start_times = intervals[:, 0]
        sort_idx_start_times = start_times.argsort()
        del start_times

        # linear scan to merge overlapping intervals
        max_num_rooms = 0
        heap_obj = Heap()
        for curr_interval_idx in sort_idx_start_times:

            curr_interval = intervals[curr_interval_idx]
            curr_interval_node = Node(
                        start_time=curr_interval[0],
                        end_time=curr_interval[1])
            del curr_interval

            # remove intervals (job which have been completed already before the start time)
            while heap_obj.num_elements_in_heap() > 0:
                min_end_time_interval_node = heap_obj.peek_min()
                if curr_interval_node.start_time >= min_end_time_interval_node.end_time:
                    heap_obj.pop_min()
                else:
                    break

            heap_obj.insert(curr_interval_node)
            max_num_rooms = max(max_num_rooms, heap_obj.num_elements_in_heap())

        return max_num_rooms

