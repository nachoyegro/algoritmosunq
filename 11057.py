import sys

LIBROS = []
PRECIO = 0 #M
CANT = 0 #N

def read_line():
    try:
        line = next(sys.stdin).strip()
        while(len(line) == 0):
            line = next(sys.stdin).strip()
        return line
    except:
        return None

def libros(m, n):
    #Ordeno e inicializo
    L.sort()
    i = 0
    j = n - 1
    a,b = 0, 0
    #Recorro hasta que llego al mismo indice
    while i < j:
        #Si la suma de los extremos actuales es menor, me muevo hacia la derecha
        if(L[i] + L[j] < m):
            i+=1
        #Si llegué, pongo esta como solución parcial y me muevo hacia el centro
        elif L[i] + L[j] == m:
            a = i
            b = j
            i+=1
            j-=1
        #Si es mayor, entonces me muevo hacia la izquierda
        else:
            j-=1
    print('Peter should buy books whose prices are %d and %d.' % (L[a], L[b]))
    print('')

if __name__ == "__main__":
    termine = False
    while True:
        try:
            CANT = int(read_line())
            L = list(map(int, read_line().split(" ")))
            PRECIO = int(read_line())
            libros(PRECIO, CANT)
        except:
            break
