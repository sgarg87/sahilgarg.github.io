import sets


class LongestSubsequence:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, sequence):
        sequence_len = len(sequence)
        longest_subsequence = ''
        longest_subsequence_len = 0

        start_idx = 0
        while start_idx < sequence_len:
            subsequence_chars_set = sets.Set()
            subsequence = ''
            subsequence_len = 0

            end_idx = start_idx
            while end_idx < sequence_len:
                curr_char = sequence[end_idx]
                if curr_char in subsequence_chars_set:
                    break
                else:
                    subsequence_chars_set.add(curr_char)
                    subsequence += curr_char
                    subsequence_len += 1
                end_idx += 1

            if subsequence_len > longest_subsequence_len:
                longest_subsequence = subsequence
                longest_subsequence_len = subsequence_len

            start_idx += 1

        print('longest_subsequence', longest_subsequence)
        return longest_subsequence_len


if __name__ == '__main__':
    longest_subsequence_obj = LongestSubsequence()

    for input in ['abcabcbb', 'bbbbb', 'pwwkew', ' ']:
        longest_subsequence = longest_subsequence_obj.lengthOfLongestSubstring(sequence=input)
        print('{} is the longest subsequence in {}.'.format(longest_subsequence, input))
