# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # corner case
        if head is None:
            return None

        prv_node = None
        # next_node = None
        curr_node = head

        while curr_node is not None:
            next_node = curr_node.next

            # delete curr_node if duplicate
            if (prv_node is not None) and (prv_node.val == curr_node.val):
                curr_node.next = None
                del curr_node
                prv_node.next = next_node
            else:
                prv_node = curr_node

            curr_node = next_node

        return head


