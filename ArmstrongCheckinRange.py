print("Enter the interval to check for Armstrong nos")
a=int(input())
b=int(input())
def acheck(a,s=0):
    n=len(a)
    for _ in range(n):
        s+=int(a[_])**n
    if s==int(a):return True
    else: return False
for _ in range(a,b+1):
    if acheck(str(_)):print(_)