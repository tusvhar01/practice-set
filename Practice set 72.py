text=input("Enter the text: ")
text=text.replace(' ','')
if len(text) > 1 and text.upper() == text[::-1].upper():
    print("It is Palindrome")
else:
    print("Not a Palindrome")
                                                # palindrome 
