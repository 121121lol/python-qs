def matcreate():	
	a=int(input("Enter number of rows: "))
	b=int(input("Enter number of columns"))
	mat=list()
	for _ in range(a):
		for __ in range(b):
			mat[a][b]=int(input("Enter Element: "))
	return mat
mat1=matcreate()
mat2=matcreate()