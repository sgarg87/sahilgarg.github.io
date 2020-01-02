import numpy as np
import heapq as h


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        print(coins, amount)

        if amount == 0:
            return 0

        if not coins:
            return -1

        num_denominations = len(coins)
        coins.sort(reverse=True)

        min_denomination = coins[-1]

        if amount < min_denomination:
            return -1

        curr_denomination_idx = 0
        curr_denomination = coins[curr_denomination_idx]
        sel_coins_heap = []

        while True:
            if curr_denomination <= amount:
                amount -= curr_denomination
                curr_denomination_tuple = (-curr_denomination, curr_denomination_idx)
                print(curr_denomination_tuple[0], amount)
                h.heappush(sel_coins_heap, curr_denomination_tuple)
            else:
                if curr_denomination_idx == (num_denominations-1):
                    if amount != 0:
                        # remove highest denomination coin
                        curr_denomination_tuple = h.heappop(sel_coins_heap)
                        if curr_denomination_tuple[0] == (-min_denomination):
                            print(amount, curr_denomination)
                            return -1
                        else:
                            amount += (-curr_denomination_tuple[0])
                            print(-curr_denomination_tuple[0], amount)
                            curr_denomination_idx = curr_denomination_tuple[1]+1
                            curr_denomination = coins[curr_denomination_idx]
                            continue
                    else:
                        break
                else:
                    curr_denomination_idx += 1
                    curr_denomination = coins[curr_denomination_idx]

        return len(sel_coins_heap)
