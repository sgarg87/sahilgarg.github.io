class MinStack(list):

    def __init__(self):
        """
        initialize your data structure here.
        """
        super().__init__()
        self.min_val = None

    def push(self, x: int) -> None:
        """
        :type x: int
        :rtype: None
        """
        if self.min_val is None:
            self.min_val = x
        else:
            self.min_val = min(self.min_val, x)
        self.append((x, self.min_val))

    def pop(self) -> None:
        """
        :rtype: None
        """
        super().pop()
        if self:
            self.min_val = self[-1][1]
        else:
            self.min_val = None

    def top(self) -> int:
        """
        :rtype: int
        """
        return self[-1][0]

    def getMin(self) -> int:
        """
        :rtype: int
        """
        return self[-1][1]
