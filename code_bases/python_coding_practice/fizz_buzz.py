class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for x in range(1, n+1):
            s = ''
            if (x % 3) == 0:
                s += 'Fizz'
            if (x % 5) == 0:
                s += 'Buzz'

            if s:
                out.append(s)
            else:
                out.append(str(x))

        return out
