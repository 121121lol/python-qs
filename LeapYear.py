a=int(input("Enter the year to check:"))
if (a%4==0 and a%100!=0) or (a%400==0 and a%100==0):
    print("Leap year")
else:print("Not leap year")