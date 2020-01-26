import collections
import heapq


class Solution(object):

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter_obj = collections.Counter(words)
        heap_word_freq = []
        for word, freq in counter_obj.items():
            heapq.heappush(heap_word_freq, (-freq, word))

        k_frequent_words = [None]*k
        for curr_idx in range(k):
            curr_word = heapq.heappop(heap_word_freq)[1]
            k_frequent_words[curr_idx] = curr_word

        return k_frequent_words

