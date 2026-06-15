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


#Lecture 4
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

#linspace
ar_lin=np.linspace(1,20,num=5)
print(ar_lin)

#Lecture 5 

1.#Random function
#rand()

import numpy as np
var=np.random.rand(4)
print(var)

varl=np.random.rand(2,5)
print(varl)

#Randn()
var2=np.random.randn(5)
print(var2)

#Rnf()
var3=np.random.ranf(4)
print(var3)

#Randint()
var4=np.random.randint(5,20,5)
print(var4)

#Lecture 6
#Data type in Numpy Array

import numpy as np

var = np.array([1, 2, 3, 4,12,13,15])
print("data type:", var.dtype)


var = np.array([1.0,1.2,1.3])
print("data type:", var.dtype)

var = np.array(["A","B","C"])
print("data type:", var.dtype)

var = np.array(["A","B","C",1,2,3,4])
print("data type:", var.dtype)

import numpy as np

X = np.array([1,2,3,4])
print("data type:", X.dtype)

X = np.array([1,2,3,4], dtype=np.int8)
print("data type:", X.dtype)
print(x)

X = np.array([1,2,3,4],dtype="f")
print("data type:", X.dtype)
print(x) 


#Lecture 7
#Arithmetic Operation in Numpy Array.
#1.(a+b) is np.add(a,b)
#2.(a-b) is np.subtract(a,b)
#3.(a*b) in np.multiply(a,b)
#4.(a/b) is np.divide(a,b)
#5.(a%b) is np.mod(a,b)
#6.(a**b) is np.power(a,b)
#7.(1/a) is np.reciprocal(a)

import numpy as np
var=np.array([1,2,3,4,5,])
varadd=var+5
print(varadd)


var1 = np.array([1,2,3,4,5,])
var2 = np.array([1,2,3,4,5,])
varadd=var1+ var2
print(varadd)

var1 = np.array([1,2,3,4,5,])
var2 = np.array([1,2,3,4,5,])
varadd=var1- var2
print(varadd)

var=np.array([1,2,3,4,5,])
varadd=var-5
print(varadd)

var=np.array([1,2,3,4,5,])
varadd=var*5
print(varadd)

var=np.array([1,2,3,4,5,])
varadd=var/5
print(varadd)

var=np.array([1,2,3,4,5,])
varadd= np.reciprocal(var)
print(varadd)



#2d array
#np.add(a,b)

var21  =np.array([[1,2,3,4,5],[1,2,3,4,5]])
var22  =np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(var21)
print()
print(var22)
print()
varadd2=var21+var22
print(varadd2)

#np.multiply(a,b)

var21  =np.array([[1,2,3,4,5],[1,2,3,4,5]])
var22  =np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(var21)
print()
print(var22)
print()
varadd2=var21*var22
print(varadd2)

#Lecture 8
# Arithmetic functions in numpy array

import numpy as np
var=np.array([1,2,3,4,5,6,7])
print("min:",np.min(var))
print("max:",np.max(var))


var=np.array([1,2,3,4,5,6,7])
print("min:",np.min(var),np.argmin(var))
print("max:",np.max(var),np.argmax(var))


var1=np.array([[2,4,3],[7,8,3]])
print(np.min(var1,axis=1))

var1=np.array([[2,4,3],[7,8,3]])
print(np.min(var1,axis=0))

var=np.array([1,2,3,4,5,6,7])
print("min:",np.min(var))
print("max:",np.max(var))
print("sqrt:",np.sqrt(var))


var2=np.array([1,2,3,4,5,6,7])
print(np.sin(var2))
print(np.cos(var2))



var2 = np.array([1,2,3,4,5,6,7])

print(np.sin(var2))
print(np.cos(var2))
print(np.cumsum(var2))

#Lecture 9
import numpy as np

var = np.array([[1,2],[1.2,3.4]])

print(var)
print()

print(var.shape)


var1 = np.array([1,2,3,4],ndmin=4)
print(var1)
print(var1.ndim)
print()
print(var1.shape)

#Reshape
var2=np.array([1,2,3,4,5,6])
x=var2.reshape(3,2)
print(x) 

var2=np.array([1,2,3,4,5,6,1,2,3])
print(var2)

print()
x=var2.reshape(3,3)
print(x)
print(x.ndim)


var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)
print(x.ndim)

print()
x1=var3.reshape(2,3,2)
print(x1)
print(x1.ndim)



var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)
print(x.ndim)

print()
x1=var3.reshape(2,3,2)
print(x1)
print(x1.ndim)

print()

one=x1.reshape(-1)
print(one)
print(one.ndim) 

 
#Lecture10 
#Broadcasting Numpy Arrays

# two rull of broadcasting 
#1.same dimensior
#2.diferent values

import numpy as np

var1 = np.array([1,2,3])

print(var1.shape)
print()
print(var1)
print()

var2 = np.array([[1],[2],[3]])

print(var1 + var2)
print()

print(var2)

print(var1+var2)

x=np.array([[1],[2]])
print(x.shape)

y=np.array([[1,2,3,],[1,2,3,]])
print(y.shape)
print(x+y)

#Lecture11
#Indexing & Slicing
#INDEXING
# 1. for 1D array
import numpy as np
var=np.array([1,2,3,4,5])
# indexing    0,1,2,3,4
# -ive indexing -5,-4,-3,-2,-1
print("1D array: ",var)
print("value of index 3: ",var[3]) # access fourth element of the array.
print("value of index -3: ",var[-3]) # access third element of the array.
# 2. for 2D array
var2=np.array([[1,2,3],[4,5,6]])
print("2D array: ",var2)
print("value of index [0][2]: ",var2[0][2]) # access first row and third column element of the array.
print("value of index [1][0]: ",var2[1][0]) # access second row and first column element of the array.
# 3. for 3D array
var=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D array: ",var)
print("value of [0,1,1]: ",var[0,1,1]) # access first block, second row and second column element of the array.
print("value of [1,0,2]: ",var[1,0,2]) # access second block, first row and third column element of the array.
#SLICING
#Parameter for slicing is [start:stop:step]
# 1. for 1D array
var=np.array([1,2,3,4,5])
# index no.   0,1,2,3,4
print("1D array: ",var)
print("slicing from index 1 to 4: ",var[1:4]) # access elements from index 1 to 3.
print("slicing from start to end: ",var[:]) # access all elements of the array.
print("slicing with step size 2: ",var[::2]) # access elements with step size 2.
# 2. for 2D array
var2=np.array([[1,2,3,5,8],[4,5,6,7,9]])
print("2D array: ",var2)
print("slicing second row: ",var2[1,:]) # access all columns of the second row.
print("slicing first column: ",var2[:,0]) # access all rows of the first column.
print("get subarray by slicing: ",var2[0:2,1:4]) # access first two rows and columns from index 1 to 3.

# Lecture 12
# Numpy iteration arrays (nditer function)
# 1. for 1D array
import numpy as np
var=np.array([3,4,7,9,2,8])
print("1D array: ",var)
print("print iteration of 1D array")
for i  in var: 
    print(i) # here we are iterating through each element of the array.   
# 2. for 2D array
var2=np.array([[1,2,3],[4,5,6]])
print("2D array: ",var2)
print("print iteration of 2D array through each row")
for i in var2:
    print(i) # here we are iterating through each row of the array. 

print("print iteration of 2D array through each element")
for k in var2:
    for j in k:
        print(j) # here we are iterating through each element of the array. 

print("iterate again by using nditer function")
for i in np.nditer(var2): # here we are iterating through each element of the array by using nditer function. it is more efficient than nested for loop.
        print(i)

print("iterate with index by using ndenumerate function")
for i,d in np.ndenumerate(var2): # here we are iterating through each element of the array with its index by using ndenumerate function.
    print(i,d) # i is the index and d is the value of the element at that index.


    # Lecture 13
#copy vs view in numpy array
import numpy as np
var=np.array([1,2,3,4,5])
co=var.copy() # here we are creating a copy of the array. it is a new array with same values as original array but it is stored in different memory location. any change in copy array will not affect original array.
var[1]=100
print("original array: ",var)
print("copy of the original array: ",co) # here we are creating a copy of the array. it is a new array with same values as original array but it is stored in different memory location. any change in copy array will not affect original array.

x=np.array([1,2,3,4,5])
vi=x.view() # here we are creating a view of the array. it is not a new array but it is just a reference to the original array. any change in view array will affect original array.
x[1]=200
print("original array: ",x)
print("view of the original array: ",vi) # here we are creating a view of the array. it is not a new array but it is just a reference to the original array. any change in view array will affect original array.
print()





