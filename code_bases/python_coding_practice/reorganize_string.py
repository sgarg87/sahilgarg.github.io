import collections
import heapq


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        n_half = int((n+1)/2)

        c_obj = collections.Counter(S)
        heap_chars = [(-c, x) for x, c in c_obj.items()]
        heapq.heapify(heap_chars)

        prv_c = 0
        prv_x = ''
        new_str = ''
        while heap_chars:
            # x is char and c is neg count
            c, x = heapq.heappop(heap_chars)
            if -c > n_half:
                return ''
            new_str += x

            if prv_c < 0:
                heapq.heappush(heap_chars, (prv_c, prv_x))

            prv_c = c+1
            prv_x = x

        return new_str
