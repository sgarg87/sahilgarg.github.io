class StringToInteger:
    def __init__(self):
        self.position_values_map = {}
        self.min_int32 = -2147483648
        self.max_in32 = 2147483647

    def get_position_value(self, position_from_right):
        assert position_from_right >= 1
        # position starts with 1
        if position_from_right in self.position_values_map:
            value = self.position_values_map[position_from_right]
        else:
            value = 10**(position_from_right-1)
            self.position_values_map[position_from_right] = value
        return value

    def extract_numeric_str(self, input_str):

        input_str = input_str.strip()

        if input_str.startswith('-'):
            is_negative_int = True
            input_str = input_str[1:]
        elif input_str.startswith('+'):
            is_negative_int = False
            input_str = input_str[1:]
        else:
            is_negative_int = False

        numeric_str = ''
        for curr_idx, curr_char in enumerate(input_str):
            if curr_char.isdigit():
                numeric_str += curr_char
            else:
                break

        return numeric_str, is_negative_int

    def map_char_to_digit(self, char):
        if char == '0':
            digit = 0
        elif char == '1':
            digit = 1
        elif char == '2':
            digit = 2
        elif char == '3':
            digit = 3
        elif char == '4':
            digit = 4
        elif char == '5':
            digit = 5
        elif char == '6':
            digit = 6
        elif char == '7':
            digit = 7
        elif char == '8':
            digit = 8
        elif char == '9':
            digit = 9
        else:
            raise AssertionError
        return digit

    def numeric_str_to_int(self, numeric_str):
        num_digits = len(numeric_str)
        if num_digits == 0:
            return 0
        else:
            int_val = 0
            for curr_idx, curr_char in enumerate(numeric_str):
                curr_digit = self.map_char_to_digit(char=curr_char)
                digit_position = num_digits-curr_idx
                curr_int_val = self.get_position_value(digit_position)
                del digit_position
                int_val += curr_digit*curr_int_val
                del curr_int_val
            return int_val

    def myAtoi(self, input_str):

        numeric_str, is_negative = self.extract_numeric_str(input_str)
        del input_str

        int_val = self.numeric_str_to_int(numeric_str=numeric_str)
        if is_negative:
            int_val *= -1

        if int_val < self.min_int32:
            return self.min_int32
        elif int_val > self.max_in32:
            return self.max_in32

        return int_val


if __name__ == '__main__':
    string_to_int_obj = StringToInteger()
    for curr_input_str in ['42', '   -42', '4193 with words', 'words and 987', '-91283472332']:
        curr_int = string_to_int_obj.myAtoi(
            input_str=curr_input_str,
        )
        print('{} ---> {}'.format(curr_input_str, curr_int))
