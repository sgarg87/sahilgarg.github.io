import copy


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            odd_node = head

        even_node = odd_node.next
        even_head = even_node

        while True:
            odd_node.next = even_node.next
            if odd_node.next is None:
                break
            else:
                odd_node = odd_node.next

            even_node.next = odd_node.next
            even_node = even_node.next
            if even_node is None:
                assert odd_node.next is None
                break

        odd_node.next = even_head

        return head
