c=int(input("Enter the decimal number: "))
def bi(c):
    if c in [1,0]: return c
    else: return f'{bi(c//2)}{c%2}'
print(bi(c))