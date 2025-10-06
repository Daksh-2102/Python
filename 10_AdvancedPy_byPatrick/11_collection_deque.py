#deque is a double-ended queue that can add and remove from both the ends
## It follows lifo method i.e last in first out


from collections import deque

d = deque()

d.append(1)
d.extend([2,3,4,5])

d.appendleft(0)
d.pop() ##pops the last elem
d.popleft() ##pops the leftmost elem
print(d)