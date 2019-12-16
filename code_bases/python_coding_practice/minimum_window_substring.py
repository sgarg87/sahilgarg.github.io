import sets


class MinimumWindowSubstring:
    def __init__(self):
        pass

    def map_of_char_input_per_target(self, input_str, target):

        target_char_map = {}
        for curr_char in target:
            if curr_char in target_char_map:
                target_char_map[curr_char] += 1
            else:
                target_char_map[curr_char] = 1

        input_char_map = {}
        for curr_char in input_str:
            if curr_char in target_char_map:
                if curr_char in input_char_map:
                    input_char_map[curr_char] += 1
                else:
                    input_char_map[curr_char] = 1

        return target_char_map, input_char_map

    def init_map_of_char_per_target(self, target_char_map):
        input_char_map = {}
        for curr_char in target_char_map:
            input_char_map[curr_char] = 0
        return input_char_map

    def contains_all_chars_in_target(self, input_char_map, target_char_map):
        for curr_char in target_char_map:
            if curr_char not in input_char_map:
                return False
            elif input_char_map[curr_char] < target_char_map[curr_char]:
                return False
        return True

    def minWindow(self, input_str, target):

        target_char_map, input_char_map = self.map_of_char_input_per_target(
            input_str=input_str,
            target=target,
        )

        is_condition_satisfied = self.contains_all_chars_in_target(
            input_char_map=input_char_map,
            target_char_map=target_char_map,
        )

        if not is_condition_satisfied:
            return ""
        else:
            input_str_len = len(input_str)

            # since the condition does satisfy
            min_window = input_str
            min_window_len = input_str_len

            window_char_map = self.init_map_of_char_per_target(target_char_map=target_char_map)
            left_idx = 0
            right_idx = 0
            window_char_map[input_str[0]] = 1
            if self.contains_all_chars_in_target(input_char_map=window_char_map, target_char_map=target_char_map):
                return input_str[0]
            is_condition_satisfied = False

            while left_idx <= right_idx:
                # print(input_str[left_idx:right_idx+1])

                if not is_condition_satisfied:
                    if right_idx == (input_str_len-1):
                        break
                    # increment right cursor
                    right_idx += 1
                    curr_char = input_str[right_idx]
                    if curr_char in target_char_map:
                        window_char_map[curr_char] += 1
                        if self.contains_all_chars_in_target(
                            input_char_map=window_char_map,
                            target_char_map=target_char_map,
                        ):
                            is_condition_satisfied = True
                    else:
                        continue
                else:
                    curr_char = input_str[left_idx]
                    if curr_char not in target_char_map:
                        left_idx += 1
                        continue
                    else:
                        window_char_map[curr_char] -= 1
                        if not self.contains_all_chars_in_target(
                            input_char_map=window_char_map,
                            target_char_map=target_char_map,
                        ):
                            curr_window_len = right_idx-left_idx+1
                            if curr_window_len < min_window_len:
                                min_window_len = curr_window_len
                                min_window = input_str[left_idx:right_idx+1]
                            left_idx += 1
                            is_condition_satisfied = False
                        else:
                            left_idx += 1

            return min_window


if __name__ == '__main__':
    S = 'ADOBECODEBANC'
    T = 'ABC'
    mws_obj = MinimumWindowSubstring()
    print(mws_obj.minWindow(
        input_str=S,
        target=T,
    ))

