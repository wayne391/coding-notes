def solution(A):
    MAX = 1000000000.
    tmp, acc, total = 0, 0, 0
   
    for a in A[::-1]:
        if a:
            tmp += 1
        else:
            acc += tmp
            total += acc
            if total > MAX:
                return -1
            tmp = 0
    return  total