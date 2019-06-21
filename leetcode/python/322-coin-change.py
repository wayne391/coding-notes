'''
Top down, too slow (1100 ms)
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        
        table = [None] * amount + [0]
    
        for i in range(amount-1, -1, -1):
            cand = []
            for step in coins:
                tmp = i + step
                if tmp <= amount and table[tmp] is not None:
                    cand.append(table[tmp])
            table[i] = min(cand) + 1  if cand else None
        return -1 if table[0] == None else table[0]