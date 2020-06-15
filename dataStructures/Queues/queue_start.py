# try out the Python queue functions
from collections import deque
# TODO: create a new empty deque object that will function as a queue
queue = deque()

# TODO: add some items to the queue
queue.append(3)
queue.append(33)
queue.append(23)
queue.append(13)
queue.append(89)
# TODO: print the queue contents
print(queue)

# TODO: pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)