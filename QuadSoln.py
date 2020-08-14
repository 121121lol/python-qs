a=float(input("Enter the coeff of x2"))
b=float(input("Enter the coeff of x"))
c=float(input("Enter constant"))
d=b**2-4*a*c
if d>=0:
    print(f"the roots are {((-1)*b+d)/2*a} and {((-1)*b-d)/2*a}")