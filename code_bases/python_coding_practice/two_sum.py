import numpy as np


class TwoSum:

    def twoSum(self, inputs, sum_for_comparison):
        # not to access any input element twice
        # exactly one solution
        # integers
        assert inputs.dtype == np.int
        hash_table = {}

        for curr_idx, curr_input in enumerate(inputs):
            complement_curr_input = sum_for_comparison-curr_input
            if complement_curr_input in hash_table:
                assert curr_idx != hash_table[complement_curr_input]
                return hash_table[complement_curr_input], curr_idx
            hash_table[curr_input] = curr_idx

        return None, None


if __name__ == '__main__':
    two_sum_obj = TwoSum()
    inputs = np.array([2, 7, 11, 15])
    print('inputs', inputs)
    for sum_for_comparison in [9, 13, 18, 17, 22, 26]:
        idx1, idx2 = two_sum_obj.find_indices_of_two_numbers_for_sum(
            inputs=inputs,
            sum_for_comparison=sum_for_comparison,
        )
        print('{}: {}, {}'.format(sum_for_comparison, idx1, idx2))

