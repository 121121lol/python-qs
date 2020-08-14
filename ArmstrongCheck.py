a=input("Enter a nuumber to check for Armstrong no")
def acheck(a,s=0):
    n=len(a)
    for _ in range(n):
        s+=int(a[_])**n
    if s==int(a):return True
    else: return False
if acheck(a):print("Armstrong")
else: print("Not Armstrong")