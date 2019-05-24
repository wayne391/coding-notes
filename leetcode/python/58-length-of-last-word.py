class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.strip(' ').split(' ')
        return 0 if not s_list else len(s_list[-1])