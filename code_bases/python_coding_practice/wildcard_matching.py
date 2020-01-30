class Solution(object):
    def recursive_match(self, s, p, memory):
        if (s, p) in memory:
            # print('Bingo!')
            return memory[(s, p)]
        # print('.................')
        # print(s, p)

        if (not s) and (not p):
            # print(s, p, True)
            memory[(s, p)] = True
            return True
        elif s and (not p):
            # print(s, p, False)
            memory[(s, p)] = False
            return False
        elif (not s) and p:
            if p == "*":
                # print(s, p, True)
                memory[(s, p)] = True
                return True
            elif p[0] not in ['*']:
                # print(s, p, False)
                memory[(s, p)] = False
                return False

        if p[0] != '*':
            # characters or ?
            if not s:
                # print(s, p, False)
                memory[(s, p)] = False
                return False
            else:
                if (p[0] != '?') and (s[0] != p[0]):
                    # print(s, p, False)
                    memory[(s, p)] = False
                    return False
                else:
                    is_match = self.recursive_match(s=s[1:], p=p[1:], memory=memory)
                    memory[(s, p)] = is_match
                    return is_match
        else:
            for i in range(len(s)+1, -1, -1):
                is_match = self.recursive_match(s=s[i:], p=p[1:], memory=memory)
                if is_match:
                    memory[(s, p)] = True
                    return True
                del is_match

            memory[(s, p)] = False
            return False

            # is_match1 = self.recursive_match(s=s, p=p[1:], memory=memory)
            # if is_match1:
            #     memory[(s, p)] = True
            #     return True
            # # del is_match1
            #
            # is_match2 = self.recursive_match(s=s[1:], p=p, memory=memory)
            # print('.................')
            # print(s, p[1:], is_match1)
            # print(s[1:], p, is_match2)
            # memory[(s, p)] = is_match2
            #
            # return is_match2

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memory = {}
        return self.recursive_match(s=s, p=p, memory=memory)
