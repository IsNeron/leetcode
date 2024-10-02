#Лучше по скорости, хуже по мемори
def squareIsWhite(coordinates: str) -> bool:
    black = ['a', 'c', 'e', 'g']
    
    if coordinates[0] in black:
        return int(coordinates[1]) % 2 == 0
    return int(coordinates[1]) % 2 == 1

#Хуже по скорости, лучше по мемори
def squareIsWhite(coordinates: str) -> bool:
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
    
    x = mapa[coordinates[0]] + int(coordinates[1])
    
    return x % 2 == 1


print(squareIsWhite('a1')) #False 
print(squareIsWhite('h3')) #True 
print(squareIsWhite('c7')) #False 