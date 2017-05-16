#PRODUCTOS = [(64, 26), (85, 22), (52, 4), (99, 18), (39, 13), (54, 9)]
#PERSONAS = [23, 20, 20, 26]
PRODUCTOS = [(72, 17), (44, 23), (31, 24)]
PERSONAS = [26]

def backtracking(num, restante):
    if num == len(PRODUCTOS):
        #Si ya termine de recorrer los productos, termino.
        return 0
    if restante < 0:
        #Si ya me pase con el peso, recorto.
        return 0
    ponerlo = backtracking(num+1, restante-weight(num)) + price(num)
    no_ponerlo = backtracking(num+1, restante)
    if ponerlo == 103:
        import pdb;pdb.set_trace()
    return max(ponerlo, no_ponerlo)

def weight(n):
    #Devuelvo el segundo elemento del par
    return PRODUCTOS[n][1]

def price(n):
    #Devuelvo el primer elemento del par
    return PRODUCTOS[n][0]

if __name__ == "__main__":
    total = 0
    for persona in PERSONAS:
        total += backtracking(0, persona)
    print(total)
