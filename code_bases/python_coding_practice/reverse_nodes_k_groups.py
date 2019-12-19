from stack import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ReverseNodesKGroups:
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
            curr_digit = curr_node.val
            assert 0 <= curr_digit <= 9
            print(curr_digit),

            curr_node = curr_node.next
        print('')

    def push_k_elements(self, stack_obj, curr_node):
        while curr_node is not None:
            if stack_obj.is_full():
                break
            else:
                stack_obj.push(curr_node)
                curr_node = curr_node.next
        return curr_node

    def elements_as_list_from_stack(self, stack_obj):
        assert not stack_obj.is_empty()
        curr_element = stack_obj.pop()
        start_node = curr_element
        while not stack_obj.is_empty():
            next_element = stack_obj.pop()
            curr_element.next = next_element
            curr_element = next_element
            del next_element
        last_node = curr_element
        if last_node is not None:
            last_node.next = None
        return start_node, last_node

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        stack_obj = Stack(max_size=k)
        curr_node = head
        head = None
        last_node_in_previous_list = None
        while curr_node is not None:
            k_plus_one_node = self.push_k_elements(stack_obj=stack_obj, curr_node=curr_node)
            if (k_plus_one_node is None) and (stack_obj.depth < k):
                if head is None:
                    head = curr_node
                else:
                    assert last_node_in_previous_list is not None
                    last_node_in_previous_list.next = curr_node
                break
            else:
                assert stack_obj.depth == k

            first_node_in_revered_k_list, last_node_in_revered_k_list = self.elements_as_list_from_stack(stack_obj)
            # print(self.print_digits(first_node_in_revered_k_list))
            assert stack_obj.is_empty()
            if head is None:
                head = first_node_in_revered_k_list

            if last_node_in_previous_list is not None:
                last_node_in_previous_list.next = first_node_in_revered_k_list
            del first_node_in_revered_k_list

            last_node_in_previous_list = last_node_in_revered_k_list
            del last_node_in_revered_k_list

            curr_node = k_plus_one_node

        return head


if __name__ == '__main__':
    inputs = [1, 2, 3, 4, 5]
    obj = ReverseNodesKGroups()
    for curr_k in [2, 3, 4]:
        head_inputs_as_list = obj.input_number_as_list(numbers_list=inputs)
        reverse_list_head = obj.reverseKGroup(head=head_inputs_as_list, k=curr_k)
        obj.print_digits(reverse_list_head)
