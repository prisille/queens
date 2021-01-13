
# the 8 queens problem

from __future__ import print_function


def check_board(i):
    for j in range(1, i):
        if (d[i-1] == d[j-1]) or (abs(d[i-1]-d[j-1]) == i-j):
            return False
    return True


def print_board():
    print("--------")

    for i in range(1, 9):
        print(d[i-1], end='')
    print()

    for i in range(1, 9):
        for j in range(1, 9):
            if (d[j-1] == i) and d[j-1] != 0:
                print("X", end='')
            else:
                print(" ", end='')
        print()


n = 0
d = [0, 0, 0, 0, 0, 0, 0, 0]
count = 0

while True:
    d[n] = d[n]+1
    if d[n] > 8:
        if n == 0:
            break
        n = n-1
    else:
        if check_board(n+1):
            if (n == 7):
                count = count+1
                print("Solution = %d" % count)
                print_board()
                print()
            else:
                n = n+1
                d[n] = 0
