def solution(N):
    k = 1
    ans = []
    while k*k < N:
        if not N % k:
            ans.append(k)
            ans.append(N/k)
        k += 1
    if k*k == N:
        ans.append(k)
    return len(ans)
