string = "Geeks"
 
def test(string):
    string = "GeeksforGeeks"
    print("Inside Function:", string)
 
# Driver's code
test(id(string))
print("Outside Function:", string)