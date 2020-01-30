class Solution(object):
    def permute_recursion(self, S, permutations_set):
        permutations_set.add(S)

        for i, x in enumerate(S):
            if x.isalpha():
                new_x = x.lower() if x.isupper() else x.upper()
                new_S = S[:i] + new_x + S[i+1:]
                del new_x
                if new_S not in permutations_set:
                    self.permute_recursion(S=new_S, permutations_set=permutations_set)
                del new_S

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        permutations_set = set()
        self.permute_recursion(S=S, permutations_set=permutations_set)
        return list(permutations_set)
