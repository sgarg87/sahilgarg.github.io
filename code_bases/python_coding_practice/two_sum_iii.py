class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number not in self.data:
            self.data[number] = 0
        self.data[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for x in self.data:
            complement_x = value-x

            if (complement_x == x) and (self.data[x] >= 2):
                return True
            elif (complement_x != x) and complement_x in self.data:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
