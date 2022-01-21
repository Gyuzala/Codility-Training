def solution(N):
    # write your code in Python 3.6
    bin_num = "{0:b}".format(N)
    bin_num = bin_num.strip("0")
    #print(bin_num)
    longest = 0
    current = 0
    for i in range(len(bin_num)):
        if bin_num[i] == "0":
            current += 1
        else:
            longest = max(longest, current)
            current = 0

    return max(longest, current)
