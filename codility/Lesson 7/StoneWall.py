def solution(H):
    stack = []
    stone = 0
    for h in H:
        if not stack or h > stack[-1]:
            stack.append(h)
            stone += 1
        elif h < stack[-1]:
            while stack and h < stack[-1]:
                stack.pop()
            if not stack or stack[-1] < h:
                stack.append(h)
                stone += 1
    return stone
