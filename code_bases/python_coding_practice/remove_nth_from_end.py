# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def _remove(self, node, n):
        if node.next is None:
            return 1, False
        else:
            rem_nodes, is_changed = self._remove(node=node.next, n=n)
            if (not is_changed) and (rem_nodes == n):
                node.next = node.next.next
                is_changed = True
            return rem_nodes+1, is_changed

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            assert n == 1
            return None

        rem_nodes, is_changed = self._remove(node=head, n=n)
        if not is_changed:
            assert rem_nodes == n
            head = head.next
        return head
