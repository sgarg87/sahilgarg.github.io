import collections
import heapq


class Solution(object):

    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        name_transactions_map = collections.defaultdict(list)
        for i, x in enumerate(transactions):
            name, time, amount, city = x.split(',')
            heapq.heappush(name_transactions_map[name], (int(time), city, i, int(amount)))

        invalid_indices = set()
        for curr_name in name_transactions_map:
            prv_x = None
            curr_transactions_heap = name_transactions_map[curr_name]
            while curr_transactions_heap:
                x = heapq.heappop(curr_transactions_heap)
                if (prv_x is not None) and (x[0] - prv_x[0] <= 60) and (x[1] != prv_x[1]):
                    invalid_indices.add(x[2])
                    invalid_indices.add(prv_x[2])
                elif x[3] > 1000:
                    invalid_indices.add(x[2])
                prv_x = x

        invalid_transactions = [transactions[i] for i in invalid_indices]

        return invalid_transactions
