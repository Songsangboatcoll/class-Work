#nested ;multiple loop
adj =["red" , "big" , "tasty"]#3 element in the list
fruits = ["aplpple", "banana","cherry", "mango"]#4 elements in the list

for x in adj:
    for y in fruits:
        print(x,y) #(3*4) print statement si executed 3*4=12 
        

for x in adj:
    print('fruits')
    for y in fruits:
        print(x,y)

for x in [0,1,2]:
    pass


