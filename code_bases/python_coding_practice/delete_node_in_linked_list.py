# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # not trail node
        assert node.next is not None

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        next_node.next = None
