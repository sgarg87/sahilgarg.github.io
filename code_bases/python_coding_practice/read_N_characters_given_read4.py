"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # number of characters read
        m = 0
        local_buf = buf[:4]

        while m < n:
            assert m <= n
            num_chars_rem = (n-m)

            num_chars_read = read4(local_buf)
            print(num_chars_rem, num_chars_read)

            if num_chars_rem > num_chars_read:
                buf[m:m+num_chars_read] = local_buf
                m += num_chars_read
                if num_chars_read < 4:
                    break
            else:
                buf[m:n] = local_buf[:num_chars_rem]
                m += num_chars_rem
                break

        return m
