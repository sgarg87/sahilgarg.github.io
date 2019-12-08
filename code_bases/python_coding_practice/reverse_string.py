import numpy as np


class ReverseString:
    def __init__(self):
        pass

    def swap_chars(self, input, i, j):
        if i < j:
            temp = input[i]
            input[i] = input[j]
            input[j] = temp
            del temp
            self.swap_chars(input, i+1, j-1)
        else:
            return

    def reverse(self, input_str):
        input = list(input_str)
        input = np.array(input)
        del input_str

        self.swap_chars(input=input, i=0, j=input.size-1)

        reverse_input_str = ''.join(input)
        del input
        print(reverse_input_str)


if __name__ == '__main__':
    input_str = 'hey how you doing?'
    reverse_string_obj = ReverseString()
    reverse_string_obj.reverse(input_str=input_str)
