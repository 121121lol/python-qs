a=int(input("Enter lower limit for prime check"))
b=int(input("Enter upper limit for prime check"))
def pcheck(num):
    if num%2!=0:
        for _ in range(3,int((num/2)+1),2):
            if num%_==0:
                return False
    else:
        return False
    return True
for _ in range(a,b+1):
    if pcheck(_):print(_)