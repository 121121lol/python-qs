set1= set(map(int,input("Enter numbers for first set").split()))
set2 = set(map(int,input("Enter numbers for second set").split()))
print("Union of set1 and set2 is",set1 | set2)
print("Intersection of set1 and set2 is",set1 & set2)
print("Difference of set1 and set2 is",set1 - set2)
print("Difference of set2 and set1 is",set2 - set1)
print("Symmetric difference of set1 and set2 is",set1 ^ set2)