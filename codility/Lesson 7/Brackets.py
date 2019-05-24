def solution(S):
    stack = []
    table = {
        '}': '{',
        ']': '[',
        ')': '('
        }
    for s in S:
        if s in '{[(':
            stack.append(s)
        else:
            if not stack or stack.pop() != table[s]:
                return 0
    return 1 if not stack else 0