# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def _reverse(self, node, m, n, i=1):
        print(node.val, i)
        if i < (m-1):
            assert node.next is not None
            self._reverse(node=node.next, m=m, n=n, i=i+1)
        else:
            if i == (m-1):
                last_node, reverse_head_node, reverse_head_node_next = self._reverse(node=node.next, m=m, n=n, i=i+1)
                node.next = reverse_head_node
                last_node.next = reverse_head_node_next
            elif i < n:
                last_node, reverse_head_node, reverse_head_node_next = self._reverse(node=node.next, m=m, n=n, i=i+1)
                last_node.next = node
                return node, reverse_head_node, reverse_head_node_next
            elif i == n:
                return node, node, node.next
            else:
                raise AssertionError

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return head
        elif m == n:
            return head

        if m > 1:
            self._reverse(node=head, m=m, n=n)
        else:
            last_node, reverse_head_node, reverse_head_node_next = self._reverse(node=head, m=m, n=n)
            head = reverse_head_node
            last_node.next = reverse_head_node_next

        return head

