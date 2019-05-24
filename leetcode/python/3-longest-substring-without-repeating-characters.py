'''
from https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1781/Python-solution-with-comments.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                # update the res
                res = max(res, i-start)
                # here should be careful, like "abba"
                start = max(start, dic[ch]+1)
            dic[ch] = i
        # return should consider the last 
        # non-repeated substring
        return max(res, len(s)-start)
'''
By this method, we can acquired the substring.
'''
# class Solution:
#     def lengthOfLongestSubstring(self, s: 'str') -> 'int':
#         max_len = 0
#         sub = ''
#         st = 0
#         for i in range(len(s)):
#             if s[i] not in sub:
#                 sub += s[i]
#             else:
#                 max_len = max(max_len, len(sub))
#                 while s[st] != s[i]:
#                     st += 1
#                 st += 1
#                 sub = s[st:i+1]
#         return max(max_len, len(sub))  