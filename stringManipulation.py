my_city = "New york"
print(type(my_city))

#Single quotes have exactly
#the same use as double quotes
my_city = 'New York'
print(type(my_city))

#setting the variable 
my_city = str("New York")
print(type(my_city))

print (" 'New york' ")
print(' "new york" ')

#string concatenation add string using +
word1 = "New "
word2 = "York"
print (word1 + word2)

word = "Rio de Janeriro"# even white space is counted
char = word[4]
print(char)
word.replace("Rio" , "Mar")
print(word)


#COUNT
print(word.count("o"))
print(word.count(' '))


print(word*3) #times printed

split_word = word.split (" ") #based on space
slit2 = word.split( " ,") #based on comma if there is and printed
print(split_word)




