def solution(A):
    flag = dict()
    for a in A:
        if a not in flag:
            flag[a] = True
    return len(flag)