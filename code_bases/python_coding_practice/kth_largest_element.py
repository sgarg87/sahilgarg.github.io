import numpy as np


class Heap:
    # min heap by default
    def __init__(self, max_size=1000):
        self.max_size = max_size
        self.data_arr = -1*np.ones(max_size, dtype=np.int)
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

    def insert(self, val):
        # added element as tbe last leaf
        self.last_idx += 1
        self.data_arr[self.last_idx] = val

        child_idx = self.last_idx
        while child_idx != 0:
            parent_idx = self._parent_idx(child_idx=child_idx)

            # swap parent and child
            if self.data_arr[child_idx] < self.data_arr[parent_idx]:
                parent_temp = self.data_arr[parent_idx]
                self.data_arr[parent_idx] = self.data_arr[child_idx]
                self.data_arr[child_idx] = parent_temp
                del parent_temp
                child_idx = parent_idx
            else:
                break

    def peek_min(self):
        if self.last_idx >= 0:
            return self.data_arr[0]
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
            min_val = self.data_arr[0]

            # last leaf value becomes root node
            self.data_arr[0] = self.data_arr[self.last_idx]
            self.last_idx -= 1

            parent_idx = 0
            while parent_idx < self.last_idx:
                left_child_idx = self._left_child_idx(parent_idx=parent_idx)
                right_child_idx = self._right_child_idx(parent_idx=parent_idx)

                is_parent_greater_than_left_else_right_child = None
                parent_val = self.data_arr[parent_idx]

                if (left_child_idx is not None) and (self.data_arr[left_child_idx] < parent_val):
                    is_parent_greater_than_left_else_right_child = True

                if (right_child_idx is not None) and (self.data_arr[right_child_idx] < parent_val):
                    if left_child_idx is None:
                        is_parent_greater_than_left_else_right_child = False
                    else:
                        if self.data_arr[right_child_idx] < self.data_arr[left_child_idx]:
                            is_parent_greater_than_left_else_right_child = False

                if is_parent_greater_than_left_else_right_child is None:
                    break
                else:
                    parent_temp = self.data_arr[parent_idx]
                    if is_parent_greater_than_left_else_right_child:
                        self.data_arr[parent_idx] = self.data_arr[left_child_idx]
                        self.data_arr[left_child_idx] = parent_temp
                        parent_idx = left_child_idx
                    else:
                        self.data_arr[parent_idx] = self.data_arr[right_child_idx]
                        self.data_arr[right_child_idx] = parent_temp
                        parent_idx = right_child_idx
                    del parent_temp
            return min_val
        else:
            assert self.last_idx == -1
            return None

    def num_elements_in_heap(self):
        return self.last_idx+1


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap_obj = Heap(max_size=k)
        for curr_idx, curr_element in enumerate(nums):
            if heap_obj.num_elements_in_heap() < k:
                heap_obj.insert(curr_element)
            else:
                min_of_heap = heap_obj.peek_min()
                if curr_element > min_of_heap:
                    removed_element = heap_obj.pop_min()
                    assert removed_element is not None
                    heap_obj.insert(curr_element)
                else:
                    pass
        return heap_obj.peek_min()


