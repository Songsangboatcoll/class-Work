#by pop(0)

queue = []
queue.append("a")
queue.append("b")
queue.append("c")
print("initial queue")
print(queue)

print("\nElements dequeued from queue")#First in first out 
print(queue.pop(0))
print(queue.pop(0)) #or popleft 
