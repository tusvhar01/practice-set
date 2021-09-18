n=int(input("Enter a no.: "))
if n<2:
    print(n,"is not a prime no.")
else:
    for i in range (2,n):
        if n%i==0:
            print(n,"is not a prime no.")
            break
    else:
        print(n,"is prime no")