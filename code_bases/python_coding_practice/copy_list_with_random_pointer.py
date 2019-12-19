# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyListWithRandomPointer:
    def __init__(self):
        pass

    def input_number_as_list(self, inputs_list):
        num_inputs = len(inputs_list)
        assert num_inputs >= 1
        list_of_nodes = []

        previous_node = None
        start_node = None
        for curr_idx, curr_item in enumerate(inputs_list):
            curr_number = curr_item[0]
            curr_node = Node(x=curr_number)
            list_of_nodes.append(curr_node)

            if curr_idx == 0:
                start_node = curr_node
            else:
                assert previous_node is not None
                previous_node.next = curr_node

            previous_node = curr_node
            del curr_node

        for curr_node_idx, curr_node in enumerate(list_of_nodes):
            curr_rnd_pointer = inputs[curr_node_idx][1]
            if curr_rnd_pointer is not None:
                curr_node.random = list_of_nodes[curr_rnd_pointer]
            else:
                curr_node.random = None

        return start_node

    def print_list(self, l1):
        assert l1 is not None
        curr_node = l1
        while curr_node is not None:
            print('({} {})'.format(curr_node.val, curr_node.random.val if curr_node.random is not None else None)),
            curr_node = curr_node.next
        print('')

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


if __name__ == '__main__':
    inputs = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    obj = CopyListWithRandomPointer()
    head = obj.input_number_as_list(inputs)
    obj.print_list(head)
    copy_head = obj.copyRandomList(head)
    obj.print_list(copy_head)
