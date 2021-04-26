names=[]
n=int(input("Enter name you want:"))
for i in range(n):
    print(i+1,"Enter name")
    names.append(input())
s=set(names)
names=list(s)
for x in names:
    print(x)
