year = int(input("Enter a year: "))

if year % 400 == 0:
    print("This year is a Leap Year")
elif year % 100 == 0:
    print("This year is a Common Year")
elif year % 4 == 0:
    print("This year is a Leap Year")
else:
    print("This year is a Common Year")
