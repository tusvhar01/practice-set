line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
print(strings)
total = 0
try:
    for substr in strings:                      # Numbers Processor
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")