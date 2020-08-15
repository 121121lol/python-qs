c=int(input("Enter the number of fibo terms in the sequence:"))
print("Fibo sequence:")
def fib(n=0,m=1,terms=1): 
    print(n+m)
    n,m=m,n+m
    if terms+1<=c:
        fib(n,m,terms+1)
fib()
