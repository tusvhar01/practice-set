text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):                         # Caesar cipher (The Caesar Cipher: encrypting a message)
        code = ord('A')
    cipher += chr(code)

print(cipher)