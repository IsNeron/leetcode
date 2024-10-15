#Лучше по скорости, хуже по мемори
def squareIsWhite(coordinate1: str, coordinate2: str) -> bool:
    mapa = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
    }
    
    x = mapa[coordinate1[0]] + int(coordinate1[1])
    y = mapa[coordinate2[0]] + int(coordinate2[1])
    
    return x % 2 == y % 2


print(squareIsWhite('a1', 'c3')) #True 
print(squareIsWhite('a1', 'h3')) #False 