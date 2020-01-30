class Solution(object):
    def read_number(self, abbr, n, j):
        numeric_str = ''
        while j < n:
            if abbr[j].isalpha():
                break
            else:
                numeric_str += abbr[j]
                j += 1
        return int(numeric_str), j

    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        m = len(word)
        n = len(abbr)

        i, j = 0, 0
        while (i < m) and (j < n):
            a = abbr[j]
            if a.isalpha():
                if a != word[i]:
                    return False
                else:
                    i += 1
                    j += 1
            else:
                if abbr[j] == '0':
                    return False

                skips, new_j = self.read_number(abbr=abbr, n=n, j=j)
                print(skips, new_j)
                if (i+skips) > m:
                    return False
                else:
                    i += skips
                    j = new_j

        print(i, j)
        if (i < m) or (j < n):
            return False
        else:
            return True
