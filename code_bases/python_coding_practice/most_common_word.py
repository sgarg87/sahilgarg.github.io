class Solution(object):
    def remove_punchtuations(self, paragraph):
        new_str = ''
        for curr_char in paragraph:
            if curr_char.isalpha() or curr_char == ' ':
                new_str += curr_char
            else:
                new_str += ' '
        return new_str

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = self.remove_punchtuations(paragraph)
        # paragraph = paragraph.strip('.')
        # paragraph = paragraph.replace(',', ' ')
        words_in_paragraph = paragraph.split(' ')
        del paragraph
        print(words_in_paragraph)

        word_count_map = {}
        for curr_word in words_in_paragraph:
            if curr_word.strip():
                if curr_word not in banned:
                    if curr_word not in word_count_map:
                        count = 0
                    else:
                        count = word_count_map[curr_word]
                    word_count_map[curr_word] = count + 1
                    print(curr_word, word_count_map[curr_word])

        print(word_count_map)
        max_count = 0
        max_count_word = None
        for curr_word in word_count_map:
            if max_count_word is None:
                max_count_word = curr_word
                max_count = word_count_map[curr_word]
            else:
                curr_count = word_count_map[curr_word]
                if curr_count > max_count:
                    max_count = curr_count
                    max_count_word = curr_word

        assert max_count_word is not None
        return max_count_word
