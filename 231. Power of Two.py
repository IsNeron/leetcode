def isPowerOfTwo(n: int) -> bool:
    if n <=0:
        return False

    return sum([int(num) for num in list("{0:b}".format(n))]) == 1

print(isPowerOfTwo(1)) #True
print(isPowerOfTwo(16)) #True
print(isPowerOfTwo(3)) #False