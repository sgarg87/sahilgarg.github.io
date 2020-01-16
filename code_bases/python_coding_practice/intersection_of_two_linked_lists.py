import random


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr_node_a = headA
        curr_node_b = headB

        if (headA is None) or (headB is None):
            return None

        num_list_changes_allowed = 2
        while True:
            if curr_node_a == curr_node_b:
                return curr_node_a
            else:
                curr_node_a = curr_node_a.next
                if curr_node_a is None:
                    if num_list_changes_allowed >= 1:
                        curr_node_a = headB
                        num_list_changes_allowed -= 1
                    else:
                        return None

                curr_node_b = curr_node_b.next
                if curr_node_b is None:
                    if num_list_changes_allowed >= 1:
                        curr_node_b = headA
                        num_list_changes_allowed -= 1
                    else:
                        return None
