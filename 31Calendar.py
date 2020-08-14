import calendar
print("Which type of calendar")
print("1 : Monthly")
print("2 : Yearly")
c=int(input())
if c==1:
	a=int(input("Enter the month number "))
	b=int(input("Enter the year"))
	print(calendar.month(b,a))
elif c==2:
	b=int(input("Enter the year"))
	print(calendar.calendar(b))
