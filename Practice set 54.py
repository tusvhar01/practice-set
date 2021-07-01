num = int(input("Enter a no."))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("no. is not a prime no." , )          # check no.prime no.
            break
    else:
        print(num,"no. is prime no.",end="")
elif num ==0 or 1 :
    print(num,"no. is neither prime nor composite no.")
else:
    print(num,"no. is a prime no.",end="")

