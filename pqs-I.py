import random
print("Hello world")
print("_________________________________________")
a=float(input("Enter first no"))
b=float(input("Enter second no"))
print(f'The sum is {a+b} ')
print("_________________________________________")
a=float(input("Enter no. to find sqrt of"))
print(f' the sqrt is {a**0.5}')
print("_________________________________________")
print("Enter sides:")
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
print(f"The area of the triangle is {(s*(s-a)*(s-b)*(s-c))**0.5}")
print("_________________________________________")
a=float(input("Enter the coeff of x2"))
b=float(input("Enter the coeff of x"))
c=float(input("Enter constant"))
d=b**2-4*a*c
if d>=0:
    print(f"the roots are {((-1)*b+d)/2*a} and {((-1)*b-d)/2*a}")
print("_________________________________________")
a=int(input("Enter first number to be swapped:"))
b=int(input("Enter second number to be swapped:"))
print(f'The value of a is {a} and b is {b}')
a,b=b,a
print(f'After swapping, the value of a is {a} and b is {b}')
print("_________________________________________")
print(random.randint(0,9))
print("_________________________________________")
km=int(input("Enter distance in km"))
print(f'{km}km is {km*0.621}miles')
print("_________________________________________")
c=float(input("Enter celcius value"))
print(f'{c}celcius is {c*1.8+32}fahrenheit')
print("_________________________________________")
a=float(input("Enter number to check whether +,- or 0"))
if a<0:print("-ve")
elif a>0: print("+ve")
elif a==0:print(0)
print("_________________________________________")
a=float(input("Enter number to check if even or odd"))
if a%2==0:
    print("Even")
else:
    print("Odd")
print("_________________________________________")
a=int(input("Enter the year to check:"))
if (a%4==0 and a%100!=0) or (a%400==0 and a%100==0):
    print("Leap year")
else:print("Not leap year")
print("_________________________________________")
a=float(input())
b=float(input())
c=float(input())
m=max(a,max(b,c))
if m==a:print(f"Max is a={a}")
elif m==b:print(f'MAx is b={b}')
elif m==c:print(f'MAx is c={c}')
print("_________________________________________")
a=int(input("Enter the number to check for prime:"))
def pcheck(num):
    if num%2!=0:
        for _ in range(3,int((num/2)+1),2):
            if num%_==0:
                return False
    else:
        return False
    return True
if pcheck(a):print("Prime")
else:print("Composite")
print("_________________________________________")
a=int(input("Enter lower limit for prime check"))
b=int(input("Enter upper limit for prime check"))
for _ in range(a,b+1):
    if pcheck(_):print(_)
print("_________________________________________")
a=int(input("Enter the number to find factorial"))
fac=1
for _ in range(2,a+1):
    fac*=_
print(f'the factorial is {fac}')
print("_________________________________________")
a=int(input("Enter the number to find multiplication table"))
for _ in range(1,11):
    print(f'{a} x {_}={a*_}')
print("_________________________________________")
a=int(input("No of terms upto which sequence is to be calculated"))
n=0
m=1
if a==1:print(0)
elif a==2:print(1)
else:
    print(0)
    print(1)
    for _ in range(a-2):
        nn=n
        n=m
        m=nn+n
        print(f'{m} ')
print("_________________________________________")
a=input("Enter a nuumber to check for Armstrong no")
def acheck(a,s=0):
    n=len(a)
    for _ in range(n):
        s+=int(a[_])**n
    if s==int(a):return True
    else: return False
if acheck(a):print("Armstrong")
else: print("Not Armstrong")
print("_________________________________________")
print("Enter the interval to check for Armstrong nos")
a=int(input())
b=int(input())
for _ in range(a,b+1):
    if acheck(str(_)):print(_)
print("_________________________________________")
a=int(input("Enter the number upto which sum is to be found"))
print(f"The sum is {a*(a+1)/2}")
print("_________________________________________")















