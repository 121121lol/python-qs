a=int(input("Enter the number whose factors you want to find"))
facs=[]
for _ in range(2,a+1):
	if a%_==0:
		facs.append(_)
print(facs)