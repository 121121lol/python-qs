vow='aeiou'
s=input().lower()
print("The count of present vowels are as follows: ")
for _ in vow:
    if _ in s: print(f'Count of {_} is {s.count(_)}')