class Solution:
    def strWithout3a3b(self, A: 'int', B: 'int') -> 'str':
        a, b = 'a', 'b'
        if B > A:
            A, B = B, A
            a, b = b, a
            
        ans = ''
        while B > 0:
            print(A, B)
            if A - B >= 2:
                ans += (a*2 + b)
                A-=2
                B-=1
                
            elif A - B == 1:
                ans += a
                A-=1
            elif A == B:
                ans += b
                B -= 1
                
        return ans + a*A