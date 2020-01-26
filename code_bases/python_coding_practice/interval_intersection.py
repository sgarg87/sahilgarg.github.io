class Solution(object):
    def simplified(self, A, B):
        n1 = len(A)
        n2 = len(B)

        intersection_list = []
        i, j = 0, 0

        while (i < n1) and (j < n2):
            print('...............')
            print(A[i], B[j])
            if A[i][1] < B[j][0]:
                print('i ends before j starts')
                i += 1
                continue
            elif B[j][1] < A[i][0]:
                print('j ends before i starts')
                j += 1
                continue
            else:
                overlap = [max(A[i][0], B[j][0]), min(A[i][1], B[j][1])]
                # i ends before j
                if A[i][1] < B[j][1]:
                    i += 1
                else:
                    if A[i][1] == B[j][1]:
                        i += 1
                    j += 1

                intersection_list.append(overlap)
                del overlap

        return intersection_list

    def intervalIntersection(self, A, B):
        # return self.sol1(A, B)
        return self.simplified(A, B)
