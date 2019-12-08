import numpy as np


class Node:
    def __init__(self, value, previous, next, is_start=False):
        self.value = value
        self.previous = previous
        self.next = next
        self.is_start = is_start


# Linked-in list implementation of Queue
class Queue:
    def __init__(self):
        self.start_node = None
        self.end_node = None

    def add_element(self, element):
        if self.start_node is None:
            node = Node(value=element, previous=None, next=None, is_start=True)
            self.start_node = node
            self.end_node = node
            del node
        else:
            node = Node(value=element, previous=self.end_node, next=None, is_start=False)
            self.end_node.next = node
            self.end_node = node
            del node

    def remove_element(self):
        if self.start_node is None:
            return None
        else:
            node = self.start_node
            if self.start_node.next is None:
                self.start_node = None
                self.end_node = None
            else:
                self.start_node = node.next
                self.start_node.previous = None
            return node.value

    def construct_queue(self, inputs):
        print('Constructing queue.')
        for curr_idx, curr_input in enumerate(inputs):
            print(curr_input),
            self.add_element(element=curr_input)
        print('')

    def traverse(self):
        curr_node = self.start_node
        print('Traversing queue.')
        while curr_node is not None:
            print(curr_node.value),
            curr_node = curr_node.next
        print('')


if __name__ == '__main__':
    inputs = np.array([4, 21, 45, 12, 3, 1])
    queue_obj = Queue()
    queue_obj.construct_queue(inputs=inputs)
    queue_obj.traverse()
