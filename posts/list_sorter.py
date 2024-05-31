list = [] # makes the list
new = []

min = 1000
while True: # while test is not q do this
    test = input("Enter numbers between 1 and 1000 (enter q to stop):")
    if test == "q":
        break

    list.append(int(test)) # adds the input to the list

length = int(len(list))

for i in range (0, length):
    for i in range (0, len(list)):
        if list[i] < min:
            min = list[i]
        new.append(int(min))
    list.remove(list[i])

print(new)