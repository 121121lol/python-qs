a=int(input("Enter the number to find factorial"))
fac=1
for _ in range(2,a+1):
    fac*=_
print(f'the factorial is {fac}')