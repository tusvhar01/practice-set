num1,num2 = eval(input())
for i in range(num1,num2+1):
    num = i

    cnt = 0
    for j in range(1,num+1):                    # to find a composite no.
        if num%j==0:
           cnt+=1

    if cnt>2:
        print(num,end=" ")