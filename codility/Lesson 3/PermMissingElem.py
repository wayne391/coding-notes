def solution(A):

    N = len(A)
    A_ = [False] * (N + 1)
    
    for a in A:
        A_[a-1] = True
        
    for i in range(N+1):
        if not A_[i]:
            return i+1