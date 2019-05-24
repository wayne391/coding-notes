def solution(A):
    N = len(A)
    peaks = []
    for i in range(1, N-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)

    for div in range(1, N+1):
        if N % div:
            continue
        groups = N/div
        flag = True
        find = 0
        for p in peaks:
            block = p//div
            if block > find:
                flag = False
                break
            if block == find:
                find += 1
        if flag and groups == find:
            return N//div

    return 0
