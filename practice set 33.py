n=input()
m=n.upper()
for letter in m:
    if letter =="A":
        print("9")                 ## replace A with any..
        continue
    elif letter =="E":
        continue
    elif letter == "O":                             ## Letter who skip vowel
        continue
    elif letter == "I":
        continue
    elif letter =="U":
        continue
    else:
        print(letter)
