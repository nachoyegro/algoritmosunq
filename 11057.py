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

def libros():
    global LIBROS, PRECIO, CANT
    #Ordeno los libros de menor a mayor
    libros = sorted(LIBROS)
    #Inicializo los libros que van a ser la solucion
    a = 0
    b = 10001
    #Recorro
    for libro in range(0, CANT):
        #tmp es el precio actual cuando le resto el libro actual
        tmp = PRECIO - libros[libro]
        #Si el precio del libro actual es mayor a lo que me queda, corto
        if tmp < libros[libro]:
            continue
        #Si el precio del libro actual es igual a lo que me queda y no hay repetidos, corto
        #Obs: Esto lo tuve que hacer porque en un caso borde donde el numero del medio es igual
        #     a lo que me queda, me lo repetia (por ejemplo, si el precio total es 160 y el libro del medio da 80,
        #     me ponia dos veces 80)
        if tmp == libros[libro] and libro < (CANT - 1) and libros[libro] != libros[libro+1]:
            continue
        #Inicializo izquierda y derecha
        izq = 0
        der = CANT - 1
        while izq < der:
            #Inicializo el medio
            mid = (izq+der)//2
            if libros[mid] < tmp:
                izq = mid+1
            else:
                der = mid
        #Despues de iterar me fijo si encontre una solucion
        if libros[der] == tmp:
            if tmp - libros[libro] < b - a:
                a = libros[libro]
                b = tmp
    print("Peter should buy books whose prices are %s and %s." % (min(a, b),max(a, b)))
    print("")

if __name__ == "__main__":
    termine = False
    while not termine:
        line = read_line()
        if not line:
            termine = True
        else:
            CANT = int(line)
            LIBROS = map(int, read_line().split(" "))
            PRECIO = int(read_line())
            libros()
