import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MergeKSortedLists:

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

    def mergeKLists_priority_queue(self, lists):
        start_node = None
        previous_node = None

        heap_size = 0
        priority_queue = []
        for curr_list_idx, curr_list_node in enumerate(lists):
            if curr_list_node is not None:
                curr_tuple = (curr_list_node.val, curr_list_idx)
                heapq.heappush(priority_queue, curr_tuple)
                heap_size += 1
                lists[curr_list_idx] = curr_list_node.next
        # print(priority_queue)

        while heap_size >= 1:

            min_val_tuple = heapq.heappop(priority_queue)
            # print('Popped', min_val_tuple)
            heap_size -= 1
            assert min_val_tuple is not None
            min_val = min_val_tuple[0]
            min_val_list_idx = min_val_tuple[1]
            del min_val_tuple

            min_val_list = lists[min_val_list_idx]
            # print('min_val_list', min_val_list)
            if min_val_list is not None:
                curr_tuple = (min_val_list.val, min_val_list_idx)
                # print('Adding', curr_tuple)
                lists[min_val_list_idx] = min_val_list.next
                del min_val_list
                heapq.heappush(priority_queue, curr_tuple)
                heap_size += 1
                del curr_tuple
            del min_val_list_idx

            curr_node = ListNode(min_val)
            del min_val

            if start_node is None:
                start_node = curr_node
            else:
                previous_node.next = curr_node
                assert previous_node.val <= curr_node.val
            previous_node = curr_node

        return start_node

    def mergeKLists_divide_and_conquer(self, lists):
        raise NotImplementedError

    def mergeKLists_standard(self, lists):
        start_node = None
        previous_node = None
        curr_idx = -1

        while True:

            curr_idx += 1

            min_val = None
            min_val_idx = None
            for curr_list_idx, curr_list_node in enumerate(lists):
                if (curr_list_node is not None) and ((min_val is None) or (curr_list_node.val < min_val)):
                    min_val = curr_list_node.val
                    min_val_idx = curr_list_idx

            if min_val is None:
                assert min_val_idx is None
                break
            else:
                assert min_val_idx is not None
                lists[min_val_idx] = lists[min_val_idx].next

            curr_node = ListNode(min_val)
            if curr_idx == 0:
                start_node = curr_node
            else:
                previous_node.next = curr_node
                assert previous_node.val <= curr_node.val
            previous_node = curr_node

        return start_node

    def mergeKLists(self, lists, algo='priority_queue'):
        if algo == 'standard':
            return self.mergeKLists_standard(lists=lists)
        elif algo == 'priority_queue':
            return self.mergeKLists_priority_queue(lists=lists)
        elif algo == 'divide_conquer':
            return self.mergeKLists_divide_and_conquer(lists=lists)
        else:
            raise AssertionError


if __name__ == '__main__':
    input1 = [1, 4, 5]
    input2 = [1, 3, 4]
    input3 = [2, 6]
    obj = MergeKSortedLists()
    lists = []
    for curr_input_idx, curr_input in enumerate([input1, input2, input3]):
        curr_list = obj.input_number_as_list(numbers_list=curr_input)
        lists.append(curr_list)
        del curr_list
    l_merged = obj.mergeKLists(lists=lists)
    obj.print_digits(l_merged)
