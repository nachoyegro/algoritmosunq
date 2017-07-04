import sys
from math import *

def read_line():
    line = next(sys.stdin).strip()
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def fun(x):
    #Escribo la funcion
    return P * exp(-1.0 * x) + Q * sin(x) + R * cos(x) +\
        S * tan(x) + T * x ** 2 + U

def biseccion():
    """
        Complejidad: O(log n), ya que voy siempre partiendo por la mitad los
        valores posibles, que seria el n
    """
    if fun(1) * fun(0) > 0:
        return 'No solution'
    epi = 1E-7
    if fun(1.0) > fun(0.0):
        mayor = 1.0
        menor = 0.0
    else:
        mayor = 0.0
        menor = 1.0

    #Mientras sean distintos
    while abs(mayor - menor) > epi:
        #Busco el medio
        medio = (mayor + menor) / 2.0
        f = fun(medio)
        #Si el resultado es mayor a 0, el medio es el mayor
        if f > 0:
            mayor = medio
        elif f < 0:
            #Sino, el medio es el menor
            menor = medio
    return '%.4f' % medio

if __name__ == "__main__":
    while True:
        try:
            P, Q, R, S, T, U = map(int, read_line().split(" "))
            print(biseccion())
        except:
            break
