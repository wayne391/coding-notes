def solution(A):
    N = [0] * len(A)
    try:
        for a in A:
            N[a-1] += 1
        for n in N:
            if n > 1 or n == 0:
                return 0
        return 1
    except:
        return 0