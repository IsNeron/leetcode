def addBinary(a: str, b: str) -> str:
    return "{0:b}".format(int(a, 2) + int(b, 2)) 

print(addBinary('11', '1')) # 100
print(addBinary('1010', '1011')) # 10101
