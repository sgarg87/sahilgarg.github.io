import numpy as np
import collections


class Solution(object):

    def __init__(self):
        pass

    def create_pattern(self, word, index):
        pattern = word[:index] + '*' + word[index+1:]
        return pattern

    def create_neighbors_dict_per_patterns_of_words(self, wordList):
        assert wordList.size >= 1
        # length should be same for all words
        k = len(wordList[0])
        patterns_map = collections.defaultdict(list)
        for curr_word in wordList:
            for curr_index in range(k):
                curr_pattern = self.create_pattern(word=curr_word, index=curr_index)
                patterns_map[curr_pattern].append(curr_word)
                del curr_pattern
        return patterns_map

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        wordList = np.array(wordList)
        print(wordList.size)
        word_len = len(wordList[0])

        patterns_map = self.create_neighbors_dict_per_patterns_of_words(wordList=wordList)

        visited = set()
        queue_obj = collections.deque(maxlen=wordList.size)
        queue_obj.append((beginWord, 1))
        visited.add(beginWord)

        while queue_obj:
            curr_str, curr_depth = queue_obj.popleft()
            neighbor_depth = curr_depth+1
            del curr_depth

            for curr_char_index in range(word_len):
                curr_pattern = self.create_pattern(word=curr_str, index=curr_char_index)
                neighboring_words = patterns_map[curr_pattern]

                for curr_neighbor_word in neighboring_words:
                    if curr_neighbor_word not in visited:
                        if curr_neighbor_word == endWord:
                            return neighbor_depth
                        else:
                            queue_obj.append((curr_neighbor_word, neighbor_depth))
                            visited.add(curr_neighbor_word)

        return 0
