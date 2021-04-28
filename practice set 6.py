# First method
i=10
while(i>=1):
    print(i,end=' ')
    i=i-1

# Second method
for i in range(10,0,-1):
    print(i)

# Third method
print([i for i in range(10,0,-1)])

# Fourth method
i=1
while(i<=10):
    print(11-i,end=' ')
    i=i+1