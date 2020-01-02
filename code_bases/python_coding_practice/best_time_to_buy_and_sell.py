class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = None
        max_profit = 0
        for curr_price in prices:
            # can sell, only if bought something
            if min_price is not None:
                curr_profit = curr_price-min_price
                max_profit = max(max_profit, curr_profit)
                del curr_profit

            # buy after the sell
            if min_price is None:
                min_price = curr_price
            else:
                min_price = min(min_price, curr_price)
        return max_profit
