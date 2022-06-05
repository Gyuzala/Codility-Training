#83%
def solution(A):
    # write your code in Python 3.6
        maximum = max(A)
        if sum(A) == maximum * (maximum+1) /2 :
             return 1
        return 0
