class Solution(object):
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words_list = S.split()
        suffix = ''
        for curr_idx, curr_word in enumerate(words_list):
            suffix += 'a'

            # consonant
            if curr_word[0] not in self.vowels:
                curr_word = curr_word[1:]+curr_word[0]

            curr_word += 'ma'
            curr_word += suffix

            words_list[curr_idx] = curr_word

        sentence = ' '.join(words_list)
        return sentence
