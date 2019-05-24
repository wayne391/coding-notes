class Solution:
    def combine(self, n, k):
        self.nums = list(range(1, n+1))
        self.n = n
        self.collect = []
        self.dfs(0, [], k)
        return self.collect

    def dfs(self, idx, sub, k):
        for i in range(idx, self.n):
            sub.append(self.nums[i])
            if k == 1:
                self.collect.append(sub[:])
            else:
                self.dfs(i+1, sub, k-1)
            sub.pop()
