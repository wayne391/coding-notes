def solution(A):
    left = 0
    right = sum(A)
    min_v = float('inf')
    
    for i in range(len(A)-1):
        left += A[i]
        right -= A[i]
        diff = abs(left - right)
        if  diff < min_v:
            min_v = diff
    return min_v