class Solution(object):
    def search_left_idx(self, nums, i, j, target):
        mid = int((i+j)/2)
        if nums[i] == target:
            return i
        elif (j-i) == 1:
            assert nums[j] == target
            return j
        elif nums[mid] < target:
            return self.search_left_idx(nums=nums, i=mid, j=j, target=target)
        elif nums[mid] == target:
            return self.search_left_idx(nums=nums, i=i, j=mid, target=target)
        else:
            raise AssertionError

    def search_right_idx(self, nums, i, j, target):
        mid = int((i+j)/2)
        if nums[j] == target:
            return j
        elif (j-i) == 1:
            assert nums[i] == target
            return i
        elif nums[mid] > target:
            return self.search_right_idx(nums=nums, i=i, j=mid, target=target)
        elif nums[mid] == target:
            return self.search_right_idx(nums=nums, i=mid, j=j, target=target)
        else:
            raise AssertionError

    def binary_search(self, nums, n, i, j, target):
        mid = int((i+j)/2)
        print('....................')
        print(i, j, mid)
        print(nums[i], nums[j], nums[mid], target)
        if nums[i] == target:
            left_idx = i
            right_idx = self.search_right_idx(nums=nums, i=i, j=j, target=target)
            return left_idx, right_idx
        elif nums[j] == target:
            left_idx = self.search_left_idx(nums=nums, i=i, j=j, target=target)
            right_idx = j
            return left_idx, right_idx
        elif nums[mid] == target:
            assert target == nums[mid]
            left_idx = self.search_left_idx(nums=nums, i=i, j=mid, target=target)
            right_idx = self.search_right_idx(nums=nums, i=mid, j=j, target=target)
            return left_idx, right_idx
        elif (j-i) <= 1:
            return -1, -1
        elif target < nums[mid]:
            return self.binary_search(nums=nums, n=n, i=i, j=mid, target=target)
        elif target > nums[mid]:
            return self.binary_search(nums=nums, n=n, i=mid, j=j, target=target)
        else:
            raise AssertionError

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1, -1

        n = len(nums)
        left_idx, right_idx = self.binary_search(nums=nums, n=n, i=0, j=n-1, target=target)
        return [left_idx, right_idx]
