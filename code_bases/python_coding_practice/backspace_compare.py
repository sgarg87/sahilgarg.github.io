class Solution(object):
    def rewrite_str(self, S, s):
        i = 0
        j = 0
        while j < s:
            if S[j] != '#':
                S[i] = S[j]
                i += 1
                j += 1
            else:
                i -= 1
                j += 1
        return i

    def rewrite_sol(self, S, T):
        s = len(S)
        t = len(T)

        s = self.rewrite_str(S, s)
        t = self.rewrite_str(T, t)
        return S[:s] == T[:t]

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = len(S)-1
        t = len(T)-1

        # count backspaces
        cs = 0
        ct = 0

        while True:

            is_change = False

            if s >= 0:
                if S[s] == '#':
                    is_change = True
                    cs += 1
                    s -= 1
                    continue
                elif cs > 0:
                    is_change = True
                    cs -= 1
                    s -= 1
                    continue

            if t >= 0:
                if T[t] == '#':
                    is_change = True
                    ct += 1
                    t -= 1
                    continue
                elif ct > 0:
                    is_change = True
                    ct -= 1
                    t -= 1
                    continue

            if (s >= 0) and (t >= 0):
                if S[s] != T[t]:
                    return False
                else:
                    is_change = True
                    s -= 1
                    t -= 1

            if not is_change:
                break

        print(s, t)
        if (s == -1) and (t == -1):
            return True
        else:
            return False
