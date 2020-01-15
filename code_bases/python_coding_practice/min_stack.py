class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_val = None
        self.stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min_val is None:
            self.min_val = x
        else:
            self.min_val = min(self.min_val, x)
        self.stack.append((x, self.min_val))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if self.stack:
            self.min_val = self.stack[-1][1]
        else:
            self.min_val = None

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
