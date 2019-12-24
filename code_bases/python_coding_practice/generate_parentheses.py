class Solution(object):
    def dfs(self, combination, count_left, count_right, max_parentheses):
        if count_left == max_parentheses:
            if count_right == max_parentheses:
                return [combination]
            else:
                branches = [0]
        else:
            branches = [0, 1]

        combinations = []
        for curr_branch in branches:
            if curr_branch == 0:
                if count_right < count_left:
                    curr_combinations = self.dfs(
                        combination=(combination + ')'),
                        count_left=count_left,
                        count_right=count_right+1,
                        max_parentheses=max_parentheses,
                    )
                    combinations += curr_combinations
                else:
                    continue
            elif curr_branch == 1:
                curr_combinations = self.dfs(
                    combination=(combination + '('),
                    count_left=count_left+1,
                    count_right=count_right,
                    max_parentheses=max_parentheses,
                )
                combinations += curr_combinations
            else:
                raise AssertionError

        return combinations

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combinations = self.dfs(combination='', count_left=0, count_right=0, max_parentheses=n)
        return combinations
