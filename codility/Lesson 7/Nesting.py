def solution(S):
    stack = 0
    for s in S:
        if s == '(':
            stack += 1
        else:
            if stack == 0:
                return 0
            stack -= 1
    return 1 if not stack else 0