class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = None
        profit = 0
        for curr_price in prices:
            if min_buy is None:
                min_buy = curr_price
                continue
            else:
                if curr_price > min_buy:
                    profit += (curr_price-min_buy)

                min_buy = curr_price

        return profit
