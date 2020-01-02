import numpy as np
import heapq as h


class Solution(object):

    def _init_amount_count_map(self):
        self.amount_count_coins_map = {}

    def _coin_change(self, coins_set, amount, min_denomination):
        # print(coins_set, amount, min_denomination)

        if amount == 0:
            return 0
        elif not coins_set:
            return None
        elif amount in coins_set:
            self.amount_count_coins_map[amount] = 1
            return 1
        elif amount < min_denomination:
            # print('amount less than minimum denomination')
            self.amount_count_coins_map[amount] = None
            return None

        min_coins = None
        for curr_coin_idx, curr_coin in enumerate(coins_set):
            curr_amount = amount-curr_coin

            if curr_amount not in self.amount_count_coins_map:
                count_of_coins_for_curr_amount = self._coin_change(
                    coins_set=coins_set,
                    amount=curr_amount,
                    min_denomination=min_denomination,
                )
            else:
                count_of_coins_for_curr_amount = self.amount_count_coins_map[curr_amount]

            if (count_of_coins_for_curr_amount is not None) \
                    and ((min_coins is None) or (count_of_coins_for_curr_amount < min_coins)):
                min_coins = count_of_coins_for_curr_amount

        if min_coins is not None:
            min_coins = min_coins + 1
        self.amount_count_coins_map[amount] = min_coins

        return min_coins

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self._init_amount_count_map()
        coins_set = set(coins)
        min_denomination = min(coins_set)
        print(min_denomination, amount)

        min_num_coins = self._coin_change(
            coins_set=coins_set,
            min_denomination=min_denomination,
            amount=amount,
        )

        if min_num_coins is None:
            return -1
        else:
            return min_num_coins
