def solution(A):
    map_ = dict()
    for a in A:
        
        if a not in map_ or (map_[a] == 0):
            map_[a] = 1
            continue
        
        if map_[a]:
            map_[a] = 0
            
    for k in map_.keys():
        if map_[k]:
            return k