l1=int(input("Enter year: "))
if(l1%4==0 and l1%100!=0):
    print("year is leap year")
elif(l1%400==0):
    print("year is leap year")
else:
    print("year is not a leap year")