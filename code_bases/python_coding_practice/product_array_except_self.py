class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_products = [0]*n
        right_products = [0]*n
        products_except_self = [0]*n

        left_product = 1
        for i in range(n):
            left_product *= nums[i]
            left_products[i] = left_product

        right_product = 1
        for i in range(n-1, -1, -1):
            right_product *= nums[i]
            right_products[i] = right_product

        for i in range(n):
            if i == 0:
                products_except_self[i] = right_products[i+1]
            elif i == (n-1):
                products_except_self[i] = left_products[i-1]
            else:
                products_except_self[i] = left_products[i-1]*right_products[i+1]

        return products_except_self
