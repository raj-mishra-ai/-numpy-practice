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

#create Numpy Array using numpy (functions)
#spacial numpy array

#zerro's array

import numpy as np

ar_zero = np.zeros(4)
ar_zero1 = np.zeros((3,4))

print(ar_zero)
print(ar_zero1)


#ones
ar_one = np.ones(4)

#empty
ar_em=np.empty(4)
print(ar_em)

#Range
ar_rn=np.arange(5)
print(ar_rn)

#Diagnal
ar_dia= np.eye(4)
print(ar_dia)

ar_dia= np.eye(3,4)
print(ar_dia)

# linspace
ar_lin=np.linspace(1,20,num=5)
print(ar_lin)
