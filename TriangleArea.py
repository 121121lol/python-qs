print("Enter sides:")
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
print(f"The area of the triangle is {(s*(s-a)*(s-b)*(s-c))**0.5}")