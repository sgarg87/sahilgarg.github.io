class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stack of left parenthesis
        stack_lp = list()

        removes = set()
        for i, x in enumerate(s):
            if x == '(':
                stack_lp.append((x, i))
            elif x == ')':
                if not stack_lp:
                    removes.add(i)
                else:
                    stack_lp.pop()
            else:
                continue

        while stack_lp:
            lp = stack_lp.pop()
            removes.add(lp[1])

        if removes:
            new_s = ''
            for i, x in enumerate(s):
                if i not in removes:
                    new_s += x
            return new_s
        else:
            return s
