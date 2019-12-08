import numpy as np


class Node:
    def __init__(self, value, top, bottom, is_top_node=False):
        self.value = value
        self.top = top
        self.bottom = bottom
        self.is_top_node = is_top_node


class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, element):
        node = Node(value=element, bottom=None, top=None, is_top_node=True)
        if self.top_node is None:
            self.top_node = node
            del node
        else:
            node.bottom = self.top_node
            self.top_node.top = node
            self.top_node.is_top_node = False

    def pop(self):
        if self.top_node is None:
            return None
        else:
            element = self.top_node.value
            if self.top_node.bottom is not None:
                new_top_node = self.top_node.bottom
                # to ensure no dangling references for the object to be freed
                self.top_node.bottom = None
                assert self.top_node.top is None

                new_top_node.top = None
                self.top_node = new_top_node
                del new_top_node
            return element

    def construct_stack(self, inputs):
        print('Constructing Stack.')
        for curr_idx, curr_input in enumerate(inputs):
            print(curr_input),
            self.push(curr_input)
        print('')


if __name__ == '__main__':
    inputs = np.array([1, 21, 45, 21, 34])
    stack_obj = Stack()
    stack_obj.construct_stack(inputs=inputs)
