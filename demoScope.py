#local variable:A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#global function
x = 300#A variable created outside of a function is global and can be used by anyone:

def myfunc():
  print("Insidefunction:",x)

myfunc()

print("outside function:",x)#statement before variable

def myfunc_global():
  global x
  x = 300

myfunc_global()

print(x)

