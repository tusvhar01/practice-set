a=input("Enter  first text: ")
b=input("Enter second text: ")
a=a.upper()
b=b.upper()
a=a.replace(' ','')
b=b.replace(' ','')
if sorted(a)==sorted(b):
    print("It is Anagram")                          # anagram
else:
    print("Not Anagram")

#An anagram is a new word formed by rearranging the letters of a word, using all the original
# letters exactly once. For example, the phrases
# "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.
