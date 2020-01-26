class Solution(object):
    def add_interval(self, intervals_set, nums, i, j):
        if not (i < j):
            return
        elif not (nums[i] < nums[j]):
            return
        else:
            intervals_to_remove = set()
            for curr_interval in intervals_set:
                if (nums[i] >= curr_interval[0]) and (nums[j] <= curr_interval[1]):
                    # subinterval
                    # no need to add this interval since a bigger once already exists
                    return
                elif (nums[i] <= curr_interval[0]) and (nums[j] >= curr_interval[1]):
                    # super interval of present interval
                    # there should be only one such interval
                    intervals_to_remove.add(curr_interval)

            for curr_interval in intervals_to_remove:
                intervals_set.remove(curr_interval)

            intervals_set.add((nums[i], nums[j]))

    def pattern_match(self, intervals_set, num_k):
        for curr_interval in intervals_set:
            if curr_interval[0] < num_k < curr_interval[1]:
                return True
        return False

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        if n <= 2:
            return False

        # 1 3 2
        # i j k
        # small value
        i = 0
        # large value
        j = 1

        # ensure that A[i] < A[j]
        while True:
            if nums[i] >= nums[j]:
                i += 1
                j += 1

                if j == n-1:
                    # k has to be larger than j
                    return False
            else:
                break

        assert nums[i] < nums[j]

        intervals_set = set()
        self.add_interval(intervals_set, nums, i, j)

        # increase the difference A[j]-A[i]
        # j is also a potential k
        k = j+1
        candidates_for_i = list()
        while j < (n-1):
            # print(i, j, k)
            assert i < j < k

            if self.pattern_match(intervals_set, nums[k]):
                return True

            if k == (n-1):
                j += 1
                self.add_interval(intervals_set, nums, i, j)
                k = j+1
                continue

            if nums[k] >= nums[j]:
                j = k
                self.add_interval(intervals_set, nums, i, j)
                k += 1
            else:
                # nums[k] < nums[j]
                # primary condition for pattern
                # curr_idx is our j
                if nums[k] > nums[i]:
                    return True
                else:
                    # nums[k] <= nums[i]
                    if nums[k] < nums[i]:
                        candidates_for_i.append(k)
                    k += 1
                    j += 1

            # adjust i if possible
            while candidates_for_i:
                if candidates_for_i[0] >= j:
                    # inner loop break
                    break
                else:
                    i = candidates_for_i.pop(0)
                    self.add_interval(intervals_set, nums, i, j)

        return False
