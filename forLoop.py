fruits = ['apple', "banana", "cherry"]#every fruits in list

for x in fruits:
    print(x)

for x in "banana":#every char in string
    print(x)


for x in fruits:
    print(x)
    if x == "banana":#stop when condition is met
        break


#continue statement, 
for x in fruits:
    if x== "banana":
        continue #escape step forward
    print(x)

#range
for x in range(6): #stop at 6 only till 5
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,30,3): #starts from 2 and increment by 3 till it hits 30(before30, 29)
    print(x)

for x in range(6):
    print(x)
else:
    print("finally finished")# only after meetin above statement
    