class Solution:
    def isPalindrome(self, x):
        x = str(x)
        N = len(x)
        for i in range(N//2):
            if x[i] != x[N-1-i]:
                return False
        return True
