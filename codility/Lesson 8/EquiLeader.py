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

    num_leader = A.count(value)
    if stack_size <= 0 or num_leader <= N//2:
        return 0

    num_left = 0
    ans = 0
    for i in range(N-1):
        if A[i] == value:
            num_left += 1
        num_right = num_leader - num_left
        if num_left > (i+1)//2 and num_right > (N-i-1)//2:
            ans += 1
    return ans
