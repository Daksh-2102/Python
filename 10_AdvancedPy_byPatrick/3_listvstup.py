#list vs tuple memory allocation
import sys
list1 = [1,2,3,4]
tuple1 = (1,2,3,4)

print(sys.getsizeof(list1),'bytes')
print(sys.getsizeof(tuple1),'bytes')

'''Clearly list contains more memory as compared to tuple '''

#also list takes more time as compare to tuple when working with large data

#So, tuple is more efficient than tuple   