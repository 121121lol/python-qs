punc = list('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
print(punc)
s=input("Enter the punctuated string: ")
print(s)
for _ in s:
	if _ in punc: s=s.replace(_,"")
print(s)

