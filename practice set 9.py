def next_Prime(n):
    while True:
        n=n+1
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return n


def prime_Producer(N):
    n=1
    count=1
    while(count<=N):
        n=next_Prime(n)
        yield n
        count=count+1
N=int(input("how many prime no. you want to generate: "))
l=[x for x in prime_Producer(N)]
print(l)

