def solution(A):
    max_ = -float('inf')
    acc = 0
    
    for a in A:
        acc += a
        acc = max(acc , a)
        max_ = max(acc, max_)
    return max_