class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MergeTwoSortedLists:

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

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_node = None
        previous_node = None
        curr_idx = -1
        while (l1 is not None) or (l2 is not None):
            curr_idx += 1

            # both lists are nonempty
            if (l1 is not None) and (l2 is not None):
                val1 = l1.val
                val2 = l2.val

                min_val = min(val1, val2)

                if min_val < val2:
                    l1 = l1.next
                else:
                    l2 = l2.next

                del val1, val2
            elif l1 is not None:
                min_val = l1.val
                l1 = l1.next
            elif l2 is not None:
                min_val = l2.val
                l2 = l2.next
            else:
                raise AssertionError

            curr_node = ListNode(min_val)
            if curr_idx == 0:
                start_node = curr_node
            else:
                previous_node.next = curr_node
                previous_node.val <= curr_node.val
            previous_node = curr_node

        return start_node


if __name__ == '__main__':
    input1 = [1, 2, 4]
    input2 = [1, 3, 4]
    obj = MergeTwoSortedLists()
    l1 = obj.input_number_as_list(numbers_list=input1)
    l2 = obj.input_number_as_list(numbers_list=input2)
    l_merged = obj.mergeTwoLists(l1=l1, l2=l2)
    obj.print_digits(l_merged)


