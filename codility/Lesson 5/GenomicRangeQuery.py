def solution(S, P, Q):
    acc = {
        1: [0],
        2: [0],
        3: [0],
        4: [0],
        }

    for s in S:
        tmp = {1: False, 2: False, 3: False, 4: False}
        if s == 'A':
            tmp[1] = True
        elif s == 'C':
            tmp[2] = True
        elif s == 'G':
            tmp[3] = True
        elif s == 'T':
            tmp[4] = True

        for i in [1, 2, 3, 4]:
            acc[i].append(acc[i][-1]+tmp[i])

    ans = []
    for k in range(len(P)):
        st, ed = P[k], Q[k]+1
        for i in [1, 2, 3, 4]:
            if acc[i][ed] - acc[i][st]:
                ans.append(i)
                break
    return ans
