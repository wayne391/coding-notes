def solution(A, B):
    res = 0
    stack = []
    for i, a in enumerate(A):
        if not stack and not B[i]:
            res += 1
            continue

        if B[i] is 1:
            stack.append((a, B[i]))
        else:
            while stack:
                if a < stack[-1][0]:
                    break
                stack.pop()
            if not stack:
                res += 1

    return res+len(stack)