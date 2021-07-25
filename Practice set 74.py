date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid data format.")
else:
    while len(date)>1:
        sum=0                               # sum of digit until it come to unit digit
        for digit in date:
            sum=sum + int(digit)
        print(sum)
        date=str(sum)
    print("Your Digit of Life is: ", date)


