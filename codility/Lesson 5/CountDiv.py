import math


def solution(A, B, K):
    st = math.ceil(A / float(K))
    ed = B // K
    return (ed - st) + 1
