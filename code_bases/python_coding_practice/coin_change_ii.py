class Solution(object):
    def dfs(self, amount, coins, min_coin, amount_count_map):
        if amount == 0:
            return 1
        elif amount < min_coin:
            return 0
        elif amount in amount_count_map:
            return amount_count_map[amount]

        count = 0
        for x in coins:
            curr_count = self.dfs(amount=(amount-x), coins=coins, min_coin=min_coin, amount_count_map=amount_count_map)
            count += curr_count

        # print(amount, count)

        return count

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        min_coin = min(coins)
        coins = set(coins)
        amount_count_map = {}
        return self.dfs(amount=amount, coins=coins, min_coin=min_coin, amount_count_map=amount_count_map)
