n=int(input("enter to check a no. is prime or not..?? "))
if(n<2):
    print("Not a Prime No.")
else:
    for i in range (2,n):
        if(n%i==0):
            print("Not a Prime No.")
            break
    else:
        print("No. is Prime")