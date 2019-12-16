class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers:

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

    def convert_list_to_int(self, l1):
        assert l1 is not None
        curr_idx = 0
        int_number = 0

        curr_node = l1
        while curr_node is not None:
            curr_digit = curr_node.val
            assert 0 <= curr_digit <= 9
            curr_int_num = curr_digit*(10**curr_idx)
            int_number += curr_int_num

            curr_node = curr_node.next
            curr_idx += 1
        return int_number

    def print_digits(self, l1):
        assert l1 is not None
        curr_node = l1
        while curr_node is not None:
            curr_digit = curr_node.val
            assert 0 <= curr_digit <= 9
            print(curr_digit),

            curr_node = curr_node.next
        print('')

    def test_addition(self, l1, l2):
        int_num1 = self.convert_list_to_int(l1)
        int_num2 = self.convert_list_to_int(l2)
        addition_two_num = int_num1 + int_num2
        return addition_two_num

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        previous_node = None
        start_node = None
        curr_idx = -1
        is_carry = False

        while is_carry or (l1 is not None) or (l2 is not None):
            curr_idx += 1
            curr_sum_digit = 0

            if l1 is not None:
                curr_sum_digit += l1.val
                l1 = l1.next

            if l2 is not None:
                curr_sum_digit += l2.val
                l2 = l2.next

            assert 0 <= curr_sum_digit <= 18
            if is_carry:
                curr_sum_digit += 1

            if curr_sum_digit > 9:
                curr_sum_digit = (curr_sum_digit%10)
                is_carry = True
            else:
                is_carry = False

            curr_sum_node = ListNode(curr_sum_digit)
            if curr_idx == 0:
                start_node = curr_sum_node
            else:
                previous_node.next = curr_sum_node
            previous_node = curr_sum_node

        return start_node


if __name__ == '__main__':
    input1 = [2, 4, 3]
    input2 = [5, 6, 4]
    obj = AddTwoNumbers()
    l1 = obj.input_number_as_list(numbers_list=input1)
    l2 = obj.input_number_as_list(numbers_list=input2)
    lsum = obj.addTwoNumbers(l1=l1, l2=l2)
    obj.print_digits(lsum)

