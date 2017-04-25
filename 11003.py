BOXES = [(19, 15), (7, 13), (5, 7), (6, 8), (1, 2)]

def backtracking(n, w):
    if n == 0:
        return 0
    return max(backtracking(n-1) + weight(n), backtracking(n-1))

def weight(n):
    #Devuelvo el primer elemento del par
    return BOXES[n][0]

def load(n):
    #Devuelvo el segundo elemento del par
    return BOXES[n][1]
