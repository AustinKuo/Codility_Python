# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    A = B = 0
    i = 1

    while (i*i) <= N:
        if N % i == 0:
            A = i
            B = int(N / i)

        i += 1

    return 2*(A+B)
