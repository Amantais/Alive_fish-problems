Task1 Bolotov Amantay

def solution(A, B):
    fish = []
    stack = []

    for x in range(len(A)):
        fish.append((B[x], A[x]))

    while fish:
        if stack and not stack[-1][0] and fish[-1][0]:
            if stack[-1][1] > fish[-1][1]:
                fish.pop()
            else:
                stack.pop()
        else:
            stack.append(fish.pop())
    return len(stack)

