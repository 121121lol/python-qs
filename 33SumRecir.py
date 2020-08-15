c=int(input("Enter the number to find sum"))
def sum(c):
    if c<=1:return 1
    else:return c+sum(c-1)
print(sum(c))