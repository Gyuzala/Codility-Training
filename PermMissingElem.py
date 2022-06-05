#100%
def solution(A):
    # write your code in Python 3.6
    n=len(A)
    total = (n+1)*(n+2)/2
    sum_A = sum(A)
    return int(total - sum_A)
