def solution(A):
    N = len(A)
    K1 = [0 for _ in range(N)]
    K2 = [0 for _ in range(N)]

    for i in range(1, N-1):
        K1[i] = max(K1[i-1]+A[i], 0)
        K2[N-1-i] = max(+ A[N-1-i]+K2[N-i], 0)

    max_v = -1
    for i in range(1, N-1):
        tmp = K1[i-1] + K2[i+1]
        if tmp > max_v:
            max_v = tmp
    return max_v
