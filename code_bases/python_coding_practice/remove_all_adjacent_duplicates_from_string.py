class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack_chars = list()
        while True:
            for x in S:
                if not stack_chars:
                    stack_chars.append(x)
                else:
                    if x == stack_chars[-1]:
                        stack_chars.pop()
                    else:
                        stack_chars.append(x)

            len_S = len(S)
            len_stack = len(stack_chars)
            S = ''.join(stack_chars[::-1])
            if len_stack == len_S:
                return S
            else:
                stack_chars = list()

