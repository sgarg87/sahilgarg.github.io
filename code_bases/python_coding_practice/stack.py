import numpy as np


class Node:
    def __init__(self, value, top, bottom, is_top_node=False):
        self.value = value
        self.top = top
        self.bottom = bottom
        self.is_top_node = is_top_node


class Stack:
    def __init__(self):
        self._top_node = None

    def push(self, element):
        node = Node(value=element, bottom=None, top=None, is_top_node=True)
        if self._top_node is None:
            self._top_node = node
            del node
        else:
            node.bottom = self._top_node
            self._top_node.is_top_node = False
            self._top_node = node

    def pop(self):
        if self._top_node is None:
            return None
        else:
            element = self._top_node.value
            if self._top_node.bottom is not None:
                new_top_node = self._top_node.bottom
                # to ensure no dangling references for the object to be freed
                self._top_node.bottom = None
                assert self._top_node.top is None

                new_top_node.top = None
                new_top_node.is_top_node = True
                self._top_node = new_top_node
                del new_top_node
            else:
                self._top_node.bottom = None
                assert self._top_node.top is None
                self._top_node = None

            # print('Popping element {}.'.format(element))
            return element

    def peek(self):
        if self._top_node is None:
            element = None
        else:
            element = self._top_node.value
        # print('Peeking element {}.'.format(element))
        return element

    def is_empty(self):
        if self._top_node is None:
            return True
        else:
            return False

    def construct_stack(self, inputs):
        print('Constructing Stack.')
        for curr_idx, curr_input in enumerate(inputs):
            print(curr_input),
            self.push(curr_input)
        print('')

    def pop_elements_one_by_one(self):
        print('Popping elements one by one.')
        while not self.is_empty():
            curr_element = self.pop()
            print(curr_element),
        print('')


if __name__ == '__main__':
    inputs = np.array([1, 21, 45, 21, 34])
    stack_obj = Stack()
    stack_obj.construct_stack(inputs=inputs)
    stack_obj.pop_elements_one_by_one()
