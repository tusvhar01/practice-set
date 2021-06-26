num1,num2 = eval(input())
if num1 > num2:
    small = num2
else:
    small = num1
for i in range(1, small+1):
    if((num1 % i == 0) and (num2 % i == 0)):        # find LCM of no.
        gcd = i
lcm = (num1*num2)//gcd
print(lcm)
