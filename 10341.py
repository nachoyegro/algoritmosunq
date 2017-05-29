import sys
from math import *

def read_line():
    line = next(sys.stdin).strip()
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def fun(x):
    return P * exp(-1.0 * x) + Q * sin(x) + R * cos(x) +\
        S * tan(x) + T * x ** 2 + U

def biseccion():
    if fun(1) * fun(0) > 0:
        return 'No solution'
    epi = 1E-7
    if fun(1.0) > fun(0.0):
        high, low = 1.0, 0.0
    else:
        high, low = 0.0, 1.0

    while abs(high - low) > epi:
        mid = (low + high) / 2.0
        f = fun(mid)
        if f > 0:
            high = mid
        elif f < 0:
            low = mid
    return '%.4f' % mid

if __name__ == "__main__":
    while True:
        try:
            P, Q, R, S, T, U = map(int, read_line().split(" "))
            print(biseccion())
        except:
            break
