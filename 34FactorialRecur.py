c=int(input("Enter the number whose factorial you want to find: "))
def fac(c):
    if c<=1: return 1
    else: return c*fac(c-1)
print(fac(c))