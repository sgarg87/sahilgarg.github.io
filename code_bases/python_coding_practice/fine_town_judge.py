class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            if N > 1:
                return -1
            else:
                return N

        non_judge_list = set()
        trusted_count_map = {}

        for curr_trust in trust:
            non_judge_list.add(curr_trust[0])

            if curr_trust[1] not in trusted_count_map:
                trusted_count_map[curr_trust[1]] = 0
            trusted_count_map[curr_trust[1]] += 1

        for curr_person in range(1, N+1):
            if curr_person not in non_judge_list:
                if (curr_person in trusted_count_map) and (trusted_count_map[curr_person] == (N-1)):
                    return curr_person

        return -1
