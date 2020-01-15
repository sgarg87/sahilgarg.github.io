class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        len_A = len(A)

        if len_A < 2:
            return -1

        A.sort()
        print(A)

        i = 0
        j = 1
        max_sum = None

        is_move_left_ptr_else_right = False
        while i < j:
            curr_sum = A[i]+A[j]
            if curr_sum < K:
                if max_sum is None:
                    max_sum = curr_sum
                else:
                    max_sum = max(max_sum, curr_sum)
            print(i, j, curr_sum)

            if curr_sum >= K:
                j -= 1
                if not is_move_left_ptr_else_right:
                    is_move_left_ptr_else_right = True
            else:
                if is_move_left_ptr_else_right:
                    i += 1
                else:
                    if j < (len_A-1):
                        j += 1
                    else:
                        is_move_left_ptr_else_right = True

        if max_sum is None:
            return -1
        else:
            return max_sum
