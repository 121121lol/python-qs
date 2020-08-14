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