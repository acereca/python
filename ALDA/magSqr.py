def magicSquare(n):
    import numpy as np
    steps = n**2

    x = int(n/2)
    y = 0
    square = np.zeros((n,n))
    for i in range(steps):
        square[y][x] = i + 1
        if (i+1) % n != 0 :
            x = x - 1
            y = y - 1
        else:
            y = y + 1
        if x < 0:
            x= x + n
        if y < 0:
            y= y + n
        if y >= n:
            y = y - n
    return square
import sys
print(magicSquare(int(sys.argv[1])))
