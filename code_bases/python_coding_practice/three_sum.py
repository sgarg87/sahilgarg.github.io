import numpy as np
from two_sum import TwoSum


class ThreeSum:
    def __init__(self):
        self.two_sum_obj = TwoSum()

    def twoSum(self, inputs, sum_for_comparison):
        # not to access any input element twice
        # todo: extend this function to deal with non-unique inputs, additional data structure to store counts of uniques and computation changes
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

    def threeSum(self, inputs):
        # not to access any input element twice
        # integers
        # assert inputs.dtype == np.int

        all_tuples = []

        for curr_idx, curr_input in enumerate(inputs):
            complement_curr_input = -curr_input
            inputs_complement = np.concatenate((inputs[:curr_idx], inputs[curr_idx+1:]))
            curr_idx2, curr_idx3 = self.two_sum_obj.twoSum(
                inputs=inputs_complement,
                sum_for_comparison=complement_curr_input,
            )

            if curr_idx2 is None:
                assert curr_idx3 is None
                continue

            if curr_idx2 >= curr_idx:
                curr_idx2 += 1

            if curr_idx3 >= curr_idx:
                curr_idx3 += 1

            curr_tuple = [
                    inputs[curr_idx],
                    inputs[curr_idx2],
                    inputs[curr_idx3],
                ]
            curr_tuple.sort()

            if curr_tuple not in all_tuples:
                all_tuples.append(curr_tuple)

        return all_tuples


if __name__ == '__main__':
    # inputs = [-1, 0, 1, 2, -1, -4]
    inputs = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    inputs = np.array(inputs)
    three_sum_obj = ThreeSum()
    all_sets = three_sum_obj.threeSum(
        inputs=inputs,
    )
    print(all_sets)

