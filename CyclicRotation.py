# 75%
def solution(A,K):
    return A[-K:] +A[:-K]

#100%
def solution(A,K):
    n = len(A)
    B = [None] * n
    for i in range(0, n):
        B[(i + K) % n] = A[i]
    return B
