def solution(A):
    vis = dict()
    for a in A:
        vis[abs(a)] = True
    return len(vis)
