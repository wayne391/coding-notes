def solution(A):
    const_max =  100001
    visit = [False] * const_max
    
    for a in A:
        if const_max > a > 0:
            visit[a-1] = True
        
    for i in range(const_max):
        if not visit[i]:
            return i+1