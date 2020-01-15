class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.data = list()
        self.data_len = 0
        self.start_idx = -1
        self.size = size
        self.average = None

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.data.append(val)
        self.data_len += 1
        print(self.data_len, val, self.start_idx, self.size)

        if self.data_len <= self.size:
            if self.data_len == 1:
                self.average = self.data[0]
            else:
                self.average = float(sum(self.data))/self.data_len
            self.start_idx = 0
        else:
            # print(self.data_len, self.size, self.start_idx)
            old_window_sum = self.average*self.size
            new_window_sum = old_window_sum-self.data[self.start_idx]+self.data[self.start_idx+self.size]
            self.average = float(new_window_sum)/self.size
            print(val, self.start_idx, old_window_sum, new_window_sum, self.average)
            self.start_idx += 1

        return self.average


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)