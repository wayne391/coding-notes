def solution(N):
    max_, tmp = 0, 0
    N = bin(N)[2:]
    for i in range(len(N)):
        if N[i] == '1':
            max_ = max(tmp, max_)
            tmp = 0
        else:
            tmp += 1
    return max_
    