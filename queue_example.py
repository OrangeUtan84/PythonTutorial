from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")
queue.append("Graham")

print(queue)

print("Removed from queue:", queue.popleft())

print("Removed from queue:", queue.popleft())

print(queue)