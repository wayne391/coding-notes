def solution(A):
    acc = [0]
    N = len(A)
    for i in range(N):
        acc.append(acc[-1] + A[i])

    min_st = -1
    min_v = float('inf')
    for i in range(N):
        sl_2, sl_3 = None, None
        if i+2 < (N+1):
            sl_2 = (acc[i+2]-acc[i]) / 2.0
        if i+3 < (N+1):
            sl_3 = (acc[i+3]-acc[i]) / 3.0
        if sl_2 is not None and sl_3 is not None:
            avg = min(sl_2, sl_3)
        elif sl_2 is not None:
            avg = sl_2
        if avg < min_v:
            min_st = i
            min_v = avg
    return min_st
