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