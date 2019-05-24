class Solution(object):
    def checkRecord(self, s):
        return (s.count('A') <= 1) and ('LLL' not in s)
        