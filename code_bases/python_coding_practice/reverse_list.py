# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def _reverse_list(self, node):
        if node.next is None:
            node.next = None
            return node, node
        else:
            last_node, head = self._reverse_list(node=node.next)
            last_node.next = node
            return node, head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        _, reverse_head = self._reverse_list(node=head)
        head.next = None
        return reverse_head
