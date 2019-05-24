def solution(A):
    N = len(A)
    stack_size = 0
    value = None

    for a in A:
        if stack_size == 0:
            stack_size += 1
            value = a
        else:
            if value != a:
                stack_size -= 1
            else:
                stack_size += 1

    if stack_size <= 0:
        return -1
    ans = -1
    cnt = 0
    for i, a in enumerate(A):
        if a == value:
            cnt += 1
            ans = i
    return -1 if cnt <= N//2 else ans
