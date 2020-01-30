import heapq


class Solution(object):
    def sol_by_heap_wrong(self, arr1, arr2, arr3):
        n1 = len(arr1)
        n2 = len(arr2)
        n3 = len(arr3)
        i, j, k = 0, 0, 0

        intersections = list()
        min_heap = list()
        while True:

            is_added = False

            if i < n1:
                is_added = True
                self._add_to_heap(min_heap, arr1[i])
                i += 1

            if j < n2:
                is_added = True
                self._add_to_heap(min_heap, arr2[j])
                j += 1

            if k < n3:
                is_added = True
                self._add_to_heap(min_heap, arr3[k])
                k += 1

            print(min_heap)

            while min_heap:
                if min_heap[0][1] == 3:
                    intersections.append(min_heap[0][0])
                    heapq.heappop(min_heap)
                else:
                    break

            if (len(min_heap) > 1) or (not is_added):
                heapq.heappop(min_heap)

            if (not min_heap) and (not is_added):
                break

        return intersections

    def _add_to_heap(self, min_heap, val):
        if (not min_heap) or (min_heap[0][0] != val):
            heapq.heappush(min_heap, [val, 1])
        else:
            min_heap[0][1] += 1

    def pointer_sols(self, arr1, arr2, arr3):
        n1 = len(arr1)
        n2 = len(arr2)
        n3 = len(arr3)
        i, j, k = 0, 0, 0

        intersections = []
        while (i < n1) and (j < n2) and (k < n3):
            if arr1[i] == arr2[j] == arr3[k]:
                intersections.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif (arr1[i] < arr2[j]) or (arr1[i] < arr3[k]):
                i += 1
            elif (arr2[j] < arr1[i]) or (arr2[j] < arr3[k]):
                j += 1
            else:
                k += 1

        return intersections

    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        # return self.sol_by_heap_wrong(arr1, arr2, arr3)
        return self.pointer_sols(arr1, arr2, arr3)
