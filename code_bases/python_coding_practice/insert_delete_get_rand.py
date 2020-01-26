import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_size = 1000
        self.data_idx_map = {}
        self.data = [0]*self.max_size
        self.num_data = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # print('insert', self.data_idx_map, self.data[:self.num_data])
        if val in self.data_idx_map:
            return False
        else:
            if self.num_data == self.max_size:
                print('Doubling memory size')
                # double the memory size
                more_data = [0]*self.max_size
                self.data += more_data
                del more_data
                self.max_size *= 2
            else:
                assert self.num_data < self.max_size

            self.data[self.num_data] = val
            self.data_idx_map[val] = self.num_data
            self.num_data += 1

            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # print('remove', self.data_idx_map, self.data[:self.num_data])

        if val not in self.data_idx_map:
            return False
        else:
            curr_idx = self.data_idx_map[val]
            # last element, simply remove
            if curr_idx == (self.num_data-1):
                self.data_idx_map.pop(val)
            else:
                last_element = self.data[self.num_data-1]

                # replaced val with last element
                self.data[curr_idx] = last_element
                self.data_idx_map.pop(val, None)
                # del val
                # print(self.data_idx_map, val)

                self.data_idx_map[last_element] = curr_idx
                del curr_idx

            self.num_data -= 1

            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        curr_element = random.choice(self.data[:self.num_data])
        # print(curr_element)
        return curr_element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()