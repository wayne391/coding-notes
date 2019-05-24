class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        table = ['' for _ in range(numRows)]
        direct = 1
        index = 0
        for char in s:
            table[index] += char 
            index += direct
            if (index == numRows):
                direct = -1
                index += direct * 2 
            if (index == -1):
                direct = 1
                index += direct * 2 
        res = ''.join(table)
        return res