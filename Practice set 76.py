l1=int(input("Enter year: "))
if(l1%4==0 and l1%100!=0):
    print("Year is leap Year")
elif(l1%400==0):
    print("Year is leap year")
else:
    print("Year is not a leap year")