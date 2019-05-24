'''
Correct Version (from https://www.martinkysel.com/codility-triangle-solution/)
'''
def solution(A):
    N = len(A)
    A.sort()
    for i in range(2, N):
        if A[i] < (A[i-1] + A[i-2]):
            return 1
    return 0

'''
Original version, in DP (Wrong!! 超時)
'''
# def solution(S, P, Q):
#     N = len(S)
#     S = list(S)
#     for i in range(N):
#         if S[i] == 'A':
#             tmp = 1
#         elif S[i] == 'C':
#             tmp = 2
#         elif S[i] == 'G':
#             tmp = 3
#         elif S[i] == 'T':
#             tmp = 4
#         S[i] = tmp
        
    
#     table = [[0 for _ in range(N)] for _ in range(N)]
#     for i in range(N-1, -1, -1):
#         table[i][i] = S[i]
#         for j in range(i+1, N):
#             table[i][j] = min(table[i+1][j], table[i][j-1])

#     ans = []
#     for p, q in zip(P, Q):
#         ans.append(table[p][q])
#     return ans