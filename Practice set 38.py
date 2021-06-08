def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem1 = elem2 = 1
    sum = 0                         ## Fabonacci no.(it is addition of last two no.)
    for i in range(3,n+1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum
for n in range(1,51):
    print(f"fibonacci of {n} is",fibonacci(n))