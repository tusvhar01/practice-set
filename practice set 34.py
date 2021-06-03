beatles=[]
print("Step 1:", beatles)
beatles.append('John Lennon')
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

list_length=len(beatles)
for i in range(list_length):
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
    print("Step 3:", beatles)
    break
del beatles[4]
del beatles[3]
print("Step 4:", beatles)

beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)                       ## Good exmple of list.


list_length=len(beatles)
print("list length is",list_length)
print("The Fab", len(beatles))