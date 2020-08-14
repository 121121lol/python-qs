while (True):
	print("Enter Choice:")
	print("0:Exit")
	print("1:Add")
	print("2:Subtract")
	print("3:Multiply")
	print("4:Divide")
	c=int(input())
	a=float(input("Enter first no"))
    b=float(input("Enter second no"))
	if c==0:break
    elif c==1:
    	print(a+b)
	elif c==2:
    	print(a-b)
	elif c==3:    
    	print(a*b)
    elif c==4:
    	if b!=0:print(a+b)
        else:print("Invalid")
    else:print("Invalid")