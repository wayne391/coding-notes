def solution(A, K):
    if not A:
        return A
    N = len(A)
    K = K % N
    return A[-K:] + A[:N-K] if K else A