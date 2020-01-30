class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        i = 1
        count = 1

        for j in range(1, n):
            if chars[j] == chars[i-1]:
                count += 1
            else:
                if count > 1:
                    str_count = str(count)
                    str_count_len = len(str_count)
                    str_count_chars = [x for x in str_count]
                    print(str_count_chars)
                    chars[i:i+str_count_len] = str_count_chars
                    i += str_count_len
                chars[i] = chars[j]
                i += 1
                count = 1

        if count > 1:
            str_count = str(count)
            str_count_len = len(str_count)
            chars[i:i+str_count_len] = [x for x in str_count]

            return i+str_count_len
        else:
            return i
