def solution(X, A):
    N = len(A)
    visit = [False] * N
    ok = 0
    
    for i in range(N):
        cur = A[i]
        if cur <= N and not visit[cur-1]:
            ok += 1
            visit[cur-1] = True
        if ok == X:
            return i
    
    return -1