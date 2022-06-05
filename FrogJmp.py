# Write your code here :-)
import math

def soultion(X,Y,D):
    if X<=Y:
        jumps=(Y-X)/D
    return math.ceil(jumps)
