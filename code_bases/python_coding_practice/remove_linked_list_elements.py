# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr_node = head
        prv_node = None

        # keep track of first node since first node may be removed
        while curr_node is not None:
            next_node = curr_node.next
            if curr_node.val == val:
                # this is head node
                if prv_node is None:
                    head = next_node
                else:
                    prv_node.next = next_node

                # remove references from curr node, that is its deletion
                curr_node.next = None
            else:
                prv_node = curr_node

            curr_node = next_node

        return head
