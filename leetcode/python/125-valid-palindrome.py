
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if (not s[left].isalnum()) or s[left].isspace():
                left += 1
                continue
            if (not s[right].isalnum()) or s[right].isspace():
                right -= 1
                continue
                    
            if s[left].lower() != s[right].lower():
                print(left, s[left].lower(), right, s[right].lower())
                return False
            left += 1
            right -= 1
        return True

'''
My original solution
Palindrome: check that if an empty string is a palindrome
'''
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_ = ''
#         for char in s:
#             if char.isalnum():
#                 s_ += char.lower()
#         for i in range(len(s_) // 2):
#             if s_[i] != s_[-1 - i]:
#                 return False
#         return True
