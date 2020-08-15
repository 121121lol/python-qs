s=list(input().split()[0])
def pali(s):	
	if s==s[::-1]:
		return True
	return False
print(pali(s))