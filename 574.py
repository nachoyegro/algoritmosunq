import sys
import fileinput

def formatted_nums(nums):
    return '+'.join([str(num) for num in nums])

def escribir_solucion(numero, sums):
    print('Sums of '+ str(numero) + ':')
    if sums:
        for s in sums:
            print(s)
    else:
        print('NONE')

def backtracking(total, cantidad_elementos, proximo_elemento, numeros_restantes, suma_actual = 0, solucion_actual=''):
    """
    *   Si la suma de los elementos de la lista actual es igual al input
    *   Agrego esa lista a la lista de listas SUMS
    """

    if suma_actual > total or solucion_actual in SUMS or proximo_elemento > cantidad_elementos:
        return
    if suma_actual == total:
        SUMS.append(solucion_actual)
        return
    if proximo_elemento == cantidad_elementos:
        return
    actual = numeros_restantes[proximo_elemento]
    solucion_con_actual = solucion_actual+'+'+str(actual) if solucion_actual else str(actual)
    backtracking(total, cantidad_elementos, proximo_elemento + 1, numeros_restantes, suma_actual + actual, solucion_con_actual)
    backtracking(total, cantidad_elementos, proximo_elemento + 1, numeros_restantes, suma_actual,solucion_actual)

if __name__ == "__main__":
    for line in sys.stdin:
        if line:
            todo = line.replace('\n', '').split(' ')
            suma = int(todo[0])
            cantidad = int(todo[1])
            if suma and cantidad:
                numeros = [int(numero) for numero in todo[2:]]
                SUMS = []
                backtracking(suma, cantidad, 0, numeros, 0, '', )
                escribir_solucion(suma, SUMS)
