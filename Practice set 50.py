number = int(input())
ans = 0
while number > 0:
    ans += number%10
    number = number//10
print(ans)                              #sum of digits
