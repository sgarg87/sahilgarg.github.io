import numpy as np
import math


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        neg_sqr_dist_to_origin = -(x**2 + y**2)
        self.dist = neg_sqr_dist_to_origin
        del neg_sqr_dist_to_origin


class Heap:
    # min heap by default
    def __init__(self, max_size=10):
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
            if self.nodes_arr[child_idx].dist < self.nodes_arr[parent_idx].dist:
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
                parent_val = self.nodes_arr[parent_idx].dist

                if (left_child_idx is not None) and (self.nodes_arr[left_child_idx].dist < parent_val):
                    is_parent_greater_than_left_else_right_child = True

                if (right_child_idx is not None) and (self.nodes_arr[right_child_idx].dist < parent_val):
                    if left_child_idx is None:
                        is_parent_greater_than_left_else_right_child = False
                    else:
                        if self.nodes_arr[right_child_idx].dist < self.nodes_arr[left_child_idx].dist:
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
            return None

    def num_elements_in_heap(self):
        return self.last_idx+1


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []

        heap_obj = Heap(max_size=K)
        for curr_point in points:
            curr_node = Node(x=curr_point[0], y=curr_point[1])
            if heap_obj.num_elements_in_heap() < K:
                heap_obj.insert(curr_node)
            else:
                min_node_from_heap = heap_obj.peek_min()
                if curr_node.dist > min_node_from_heap.dist:
                    removed_from_heap = heap_obj.pop_min()
                    assert removed_from_heap is not None
                    heap_obj.insert(curr_node)

        closest_points = []
        for curr_idx in range(K):
            curr_node = heap_obj.pop_min()
            closest_points.append([curr_node.x, curr_node.y])

        return closest_points
