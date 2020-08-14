a=list(map(int,input("Enter numbers whose divisibility is to be checked").split()))
b=int(input("Enter the number against which divisibility will be checked"))
print(f'The numbers divisible by {b} are:')
for _ in a:
	if _%b==0:print(_)