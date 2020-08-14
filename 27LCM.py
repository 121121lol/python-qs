import math
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print(f"The LCM  is {abs(a*b)//math.gcd(a,b)}")