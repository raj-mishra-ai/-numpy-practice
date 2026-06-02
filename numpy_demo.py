#Lecture 1
import numpy as np
x = np.array([1,2,3])
print(x)
print(type(x))
y = [1,2,3,4,5]
print(y)
print(type(y))          

#Lecture 2
import timeit  
execution_time = timeit.timeit(
    '[j**4 for j in range(1,2)]',
    number=10000
)

print(execution_time)

import numpy as np
import timeit

result = timeit.timeit(
    "np.arange(1,2)**4",
    globals=globals(),
    number=10000
)

print(result)

#Lecture 3 (creating numpy arrays)
#  Type of Array
#1d array
import numpy as np

x = [1,2,3,4]
y = np.array([1,2,3,4])

print(y)
print(type(y))
print(y.ndim)

#2d array
ar2=np.array([[1,2,3,4,],[1,2,3,4,]])
print(ar2)
print(ar2.ndim)

#3d array
ar3=np.array ([[[1,2,3,4,],[1,2,3,4,],[1,2,3,4]]])
print(ar3)
print(ar3.ndim)

#multidim array
import numpy as np

arn = np.array([1,2,3,4], ndmin=20)

print(arn)
print(arn.ndim)



