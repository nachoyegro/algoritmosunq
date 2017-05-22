BOXES = [(19, 15), (7, 13), (5, 7), (6, 8), (1, 2)]
mem = {}

def backtracking(n, w):
	#Si llegue al final, corto
	if n == len(BOXES):
		return 0
	#Si el peso acumulado es mayor que lo que soporta la caja actual, corto
	if load(n) < w:
		return -1
	return max(1 + backtracking(n+1, w+weight(n)), backtracking(n+1, w))

def weight(n):
    #Devuelvo el primer elemento del par
    return BOXES[n][0]

def load(n):
    #Devuelvo el segundo elemento del par
    return BOXES[n][1]

if __name__ == "__main__":
	mem = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}}
	for i in range(0, len(BOXES)):
		print(backtracking(i, 0))
