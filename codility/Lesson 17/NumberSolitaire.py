def solution(A):
    N = len(A)
    table = [A[0]]
    for i in range(1, N):
        st = max(0, i-6)
        table.append(max(table[st:i]) + A[i])
    return table[-1]