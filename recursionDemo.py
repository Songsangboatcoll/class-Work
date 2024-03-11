def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = 10
print("Fibonacci sequence:")
for i in range(n):
    print(fib(i))
    #print(i)
