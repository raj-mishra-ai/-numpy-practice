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
# Array
import numpy as np

x = [1,2,3,4]
y = np.array([1,2,3,4])

print(y)
print(type(y))




