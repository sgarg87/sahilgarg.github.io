class Solution(object):
    def dynamic_program(self, s, n, i, memory):
        if i in memory:
            return memory[i]

        if i == n:
            count = 1
        elif i > n:
            raise AssertionError
        else:
            x = s[i]
            if x == '0':
                count = 0
            else:
                count = 0
                if (i < n-1) and ((x == '1') or ((x == '2') and (s[i+1] not in ['7', '8', '9']))):
                    count2d = self.dynamic_program(s=s, n=n, i=i+2, memory=memory)
                    count += count2d
                    del count2d

                count1d = self.dynamic_program(s=s, n=n, i=i+1, memory=memory)
                count += count1d
                del count1d

        memory[i] = count

        return count

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memory = {}
        return self.dynamic_program(s=s, n=n, i=0, memory=memory)
