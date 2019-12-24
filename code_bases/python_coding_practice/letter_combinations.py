class Solution(object):
    def __init__(self):
        self.digit_alphabets_map = {}
        self.digit_alphabets_map['2'] = ['a', 'b', 'c']
        self.digit_alphabets_map['3'] = ['d', 'e', 'f']
        self.digit_alphabets_map['4'] = ['g', 'h', 'i']
        self.digit_alphabets_map['5'] = ['j', 'k', 'l']
        self.digit_alphabets_map['6'] = ['m', 'n', 'o']
        self.digit_alphabets_map['7'] = ['p', 'q', 'r', 's']
        self.digit_alphabets_map['8'] = ['t', 'u', 'v']
        self.digit_alphabets_map['9'] = ['w', 'x', 'y', 'z']
        self.depth_branches_map = None
        self.max_depth = None

    def dfs(self, combination='', depth=0):
        if depth > self.max_depth:
            assert depth not in self.depth_branches_map
            return [combination]

        branches = self.depth_branches_map[depth]
        letter_combinations = []
        for curr_branch in branches:
            curr_str = combination + curr_branch
            curr_lc = self.dfs(combination=curr_str, depth=depth + 1)
            letter_combinations += curr_lc

        return letter_combinations

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        depth_branches_map = {}
        for curr_digit_idx, curr_digit in enumerate(digits):
            curr_digit_letters = self.digit_alphabets_map[curr_digit]
            depth_branches_map[curr_digit_idx] = curr_digit_letters
        self.depth_branches_map = depth_branches_map
        self.max_depth = len(digits)-1

        combinations = self.dfs()
        return combinations
