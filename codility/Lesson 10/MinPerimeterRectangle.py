def solution(N):
    k = 1
    ans = float('inf')
    while k*k <= N:
        if not N % k:
            tmp = k + N/k
            if ans > tmp:
                ans = tmp
        k += 1
    return int(ans*2)
