'''
BFS very fast (DP不一定最快)
'''
class Solution:
    def coinChange(self, coins, amount):
        level = seen = {0}
        number = 0
        while level:
            if amount in level:
                return number
            level = {a+c for a in level for c in coins if a+c <= amount} - seen
            seen |= level
            number += 1
        return -1

'''
BFS https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution
easy to understand
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1

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