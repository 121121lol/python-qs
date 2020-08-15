a=int(input("Enter number of rows: "))
b=int(input("Enter number of columns"))
def matcreate():	
	mat=list()
	for _ in range(a):
		matt=list()
		for __ in range(b):
			matt.append(int(input("Enter Element: ")))
		mat.append(matt)
	return mat
mat1=matcreate()
mat2=matcreate()
result=list()
print("The resultant matrix is :") 
for x in range(a):
    ss=''
    for y in range(b):
        s=0
        for z in range(b):
           s += mat1[x][z] * mat2[z][y]
        ss+=f'{s} '
    print(ss)