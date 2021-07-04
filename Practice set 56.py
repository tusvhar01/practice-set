address=input()
for i in range(len(address)):
    if address[i].isnumeric():
        break
print(address[i:],end="")                       #enter string and integer output will be always integer
