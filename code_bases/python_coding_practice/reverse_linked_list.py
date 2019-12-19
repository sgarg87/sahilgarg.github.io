# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ReverseLinkedList:
    def __init__(self):
        pass

    def input_number_as_list(self, numbers_list):
        assert len(numbers_list) >= 1
        previous_node = None
        start_node = None
        for curr_idx, curr_number in enumerate(numbers_list):
            curr_node = ListNode(x=curr_number)
            if curr_idx == 0:
                start_node = curr_node
            else:
                assert previous_node is not None
                previous_node.next = curr_node
            previous_node = curr_node
            del curr_node
        return start_node

    def print_digits(self, l1):
        assert l1 is not None
        curr_node = l1
        while curr_node is not None:
            print(curr_node.val),
            curr_node = curr_node.next
        print('')

    def reverseList(self, head, is_head_node=True):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        next_node = head.next
        if is_head_node:
            head.next = None
            if next_node is None:
                return head
        else:
            assert next_node is not None

        if next_node.next is None:
            # print(head.val)
            next_node.next = head
            return next_node
        else:
            # print((head.val, next_node.val))
            reverse_head = self.reverseList(next_node, is_head_node=False)
            next_node.next = head
            return reverse_head


if __name__ == '__main__':
    inputs = [1, 2, 3, 4, 5]
    obj = ReverseLinkedList()
    head_inputs_as_list = obj.input_number_as_list(numbers_list=inputs)
    obj.print_digits(head_inputs_as_list)
    reverse_list_head = obj.reverseList(head=head_inputs_as_list)
    obj.print_digits(reverse_list_head)
