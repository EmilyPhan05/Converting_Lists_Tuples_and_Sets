import random

#creates the initial list
start = [0] * 30

#fills the initial list with random values
for i in range(len(start)):
    start[i] = random.randint(0, 100)


#creates a temporary list to later convert to a tuple
tempList = [0] * len(start)

#fills the temporary list with the same values as the first list
for i in range(len(start)):
    tempList[i] = start[i]

#makes a tuple out of the temporary list
tup = tuple(tempList)


#creates the set
fin = set()

#adds all the non duplicate values in the list and tuple to the set
for i in range(len(tempList)):
    fin.add(tempList[i])

#prints everything
print(start)
print(tup)
print(fin)