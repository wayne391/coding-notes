def solution(N, A):
    counter = [0] * N
    max_ = 0
    flag = False
    for m in A:
        if m != N+1:
            flag = True
            counter[m-1] += 1
            if counter[m-1] > max_:
                max_ = counter[m-1]
        else:
            if flag:
                counter = [max_] * N
                flag = False  
            else:
                continue
    return counter