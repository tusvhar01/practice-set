school_data={}

while True:
    name=input("Enter student name: ")
    if name=="":
        break

    score=int(input("Enter score from 0 to 10: "))        # school data demo
    if score not in range (0,11):
        break

    if name in school_data:
        school_data[name]+=(score,)
    else:
        school_data[name]=(score,)

for name in sorted(school_data.keys()):
    adding=0
    counter=0
    for score in school_data[name]:
        adding+=score
        counter+=1
    print(name,":",adding/counter)