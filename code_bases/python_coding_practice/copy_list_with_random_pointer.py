# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        if hasattr(head, 'copy') and (head.copy is not None):
            return head.copy
        else:
            # print(head.val)

            copy_node = Node(x=head.val)
            head.copy = copy_node

            if head.next is not None:
                copy_node.next = self.copyRandomList(head.next)

            if head.random is not None:
                copy_node.random = self.copyRandomList(head.random)

            return copy_node


