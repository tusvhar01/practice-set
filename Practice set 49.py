N = int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j <= i:
            print("*", end='')
        else:                           # make pyramid by input
            print(" ", end='')

    print()
