# python3

### START OF PROGRAM ###
n = int(input())

# Create an empty dictionary
phoneBook = {}

for i in range(n):
    request = [str(x) for x in input().split()]
    if request[0] == "add":             # add
        phoneBook[request[1]] = request[2]
    elif request[0] == "find":          # find
        number = request[1]
        phoneBook.setdefault(number,None)
        person = phoneBook[number]
        if person != None:
            print(person)
        else:
            print("not found")
    else:                               # delete
        number = request[1]
        phoneBook.pop(number, None)
