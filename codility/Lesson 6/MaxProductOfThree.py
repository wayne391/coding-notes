def mul(tmp):
    return tmp[0] * tmp[1] * tmp[2]

def solution(A):
    A.sort()
    return max(mul(A[-3:]), mul(A[:2]+[A[-1]]))