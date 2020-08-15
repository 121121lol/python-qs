mat=list()
a=int(input("Enter number of rows: "))
b=int(input("Enter number of columns"))
for _ in range(a):
	matt=list()
	for __ in range(b):
		matt.append(int(input("Enter Element: ")))
	mat.append(matt)
print("Transpose of matix is : ")
for x in range(a):
	s=''
	for y in range(b):
		s+=f'{((-1)**(x+y))*(mat[y][x])} '
	print(s)

