def myAtoi(s: str) -> int:
    negative = False
    for c in s:
        if c.isspace():
            continue
        if c
    



print(myAtoi('42'))
print(myAtoi('   -042'))
print(myAtoi('1337c0d3'))
print(myAtoi('0-1'))
print(myAtoi('words and 987'))