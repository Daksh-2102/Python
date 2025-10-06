#deque is a double-ended queue that can add and remove from both the ends
## It follows lifo method i.e last in first out


from collections import deque

d = deque()

d.append(1)
d.extend([2,3,4,5])

d.appendleft(0)
d.pop() ##pops the last elem
d.popleft() ##pops the leftmost elem

d.extendleft((1,1,1,10,11))

print(f"Elements before rotating : {d}")

print(f"count = {d.count(1)}")  #prints the count of the no.

d.rotate(2) #rotates the deque by one step if no value assigned else assign the rotating value, then it will ]rotate that much time
print(f"Elements after rotating  : {d}")