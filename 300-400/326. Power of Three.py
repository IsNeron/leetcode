def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    
    while n > 1:
        if n % 3 != 0:
            return False

        n = n / 3

    return True


print(isPowerOfThree(27)) #True
print(isPowerOfThree(0)) #False
print(isPowerOfThree(-1)) #False