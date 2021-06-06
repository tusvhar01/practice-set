def factorial(n):
    if n<0:
        return None
    if n<2:
        return 1
    product=1                 ## Factorial of no. by using function
    for i in range(2,n+1):
        product*=i
    return product
n=int(input("Enter no.: "))


for n in range(1,n+1):  # testing
    print(f"fac of {n} is",factorial(n))
