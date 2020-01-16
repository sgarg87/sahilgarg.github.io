# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def compute_len_of_linked_list(self, head):
        curr_node = head

        len_of_list = 0
        while curr_node is not None:
            len_of_list += 1
            curr_node = curr_node.next

        return len_of_list

    def is_palindrome_using_stack(self, head):
        if head is None:
            return True

        len_of_list = self.compute_len_of_linked_list(head=head)
        if len_of_list == 1:
            return True

        first_half = int(len_of_list/2)
        print(len_of_list, first_half)
        if (len_of_list % 2) == 0:
            is_odd_length_else_even = False
        else:
            is_odd_length_else_even = True

        # put first half to stack
        stack = list()
        count = 0
        curr_node = head
        while count < first_half:
            assert curr_node is not None
            stack.append(curr_node.val)
            curr_node = curr_node.next
            count += 1

        # skip the middle node
        if is_odd_length_else_even:
            curr_node = curr_node.next

        while curr_node is not None:
            top_val_from_stack = stack.pop()
            if curr_node.val != top_val_from_stack:
                return False
            else:
                curr_node = curr_node.next
        if stack:
            return False
        else:
            return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.is_palindrome_using_stack(head=head)
