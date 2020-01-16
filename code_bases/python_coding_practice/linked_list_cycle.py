# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        elif head.next is None:
            return False

        curr_node_slow = head
        curr_node_fast = head

        while True:
            assert (curr_node_slow is not None) and (curr_node_fast is not None)

            # move slow node
            curr_node_slow = curr_node_slow.next
            if curr_node_slow is None:
                return False

            # move fast node
            curr_node_fast = curr_node_fast.next
            if curr_node_fast is not None:
                curr_node_fast = curr_node_fast.next
                if curr_node_fast is None:
                    return False
            else:
                return False

            if curr_node_slow == curr_node_fast:
                return True
