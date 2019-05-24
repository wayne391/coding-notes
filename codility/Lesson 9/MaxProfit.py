def solution(A):
    if not A:
        return 0
    min_value = A[0]
    max_profit = 0
    
    for i in range(1, len(A)):
        profit = A[i] - min_value
        min_value = min(min_value, A[i])
        max_profit = max(max_profit, profit)
    
    return max_profit