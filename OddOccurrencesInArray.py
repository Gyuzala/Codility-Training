# 66%
def solution(A):
    for i in range(len(A)):
        count = A.count(A[i])
        if count % 2 != 0:
            return A[i]



