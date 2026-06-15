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

# Lecture 14
# Join and splint functions of numpy array.
# Join array
# 1. for 1D array
import numpy as np
var1=np.array([3,4,6,9])
var2=np.array([6,2,8,1])
ar=np.concatenate((var1,var2))
print("var1: ",var1)
print("var2 :",var2)
print("concatination: ",ar)
print()
# 2. for 2D array
var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar=np.concatenate((var1,var2))
print("var1: ",var1)
print("var2 :",var2)
print("concatination along with both row and colunm: ",ar) # here it concatenate along with axis-0(colunm) and axis-1(row) of array.
print()

var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar=np.concatenate((var1,var2),axis=1)# it will concatenate along with row.
print("var1: ",var1)
print("var2 :",var2)
print("concatenate along with row: ",ar)
print()

var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar=np.concatenate((var1,var2),axis=0)# it will concatenate along with colunm.
print("var1: ",var1)
print("var2 :",var2)
print(" concatenate along with colunm: ",ar)
print()
# merging array using stack function.
var1=np.array([[3,4,6,9],[5,6,9,3]])
var2=np.array([[6,2,8,1],[5,2,8,5]])
ar1=np.stack((var1,var2))# merge along both row and colunm.
ar2=np.hstack((var1,var2))# merge along row.
ar3=np.vstack((var1,var2))# merge along colunm.
ar4=np.dstack((var1,var2))# merge along height.
print("var1: ",var1)
print("var2 :",var2)
print("merge array by using stack function: ",ar1)
print("merge array horizontally(row): ",ar2)
print("merge array vertically(colunm): ",ar3)
print("merge array along with height: ",ar4)
print()
#Splint array
# 1. 1D array
import numpy as np
var=np.array([4,6,9,3])
print("1D array: ",var)
ar=np.array_split(var,2)
print("splited array: ",ar)
print("datatype of splited array: ",type(ar))
print("access specified array[1]: ",ar[1])
print()
# 2. for 2D array
var=np.array([[3,4,5,6],[8,9,1,2]])
print("2D array: ",var)
ar=np.array_split(var,2)
ar=np.array_split(var,2,axis=1) #split along axis.
print("splite 2D array along axis: ",ar)
print()

# Lecture 15
# Numpy arrays function.
# 1. Search(search an array for a certain value, and return the indexes that get a match)
import numpy as np
var=np.array([3,5,7,8,7,9])
print("array: ",var)
x=np.where(var==7) # here it will find 7 and return it's index value.
print("search 7: ",x)
print()
# 2. Search sorted array(it performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.)
var1=np.array([2,4,6,7,8,9])
print("array: ",var1)
x1=np.searchsorted(var1,3) # it will return the index value of where 3 will insert so that it would be in sorted order.
x2=np.searchsorted(var1,[1,3,5],side="right")
print("give index value of [3]: ",x1)
print("give index value of [1,3,5]: ",x2)
print()
# 3. sort(Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical,ascending or descending.)
var2=np.array([2,4,1,6,7,8,5,13,9])
print("array: ",var2)
print("sorted array: ", np.sort(var2))

var3=np.array(["f","j","a","t","c","e"])
print("array: ",var3)
print("sorted array: ", np.sort(var3))
print()

var2=np.array([[2,4,1,6],[7,8,5,13]])
print("2D array: ",var2)
print("sorted 2D array: ", np.sort(var2))
print()
# 4. Filter array(Getting some elements out of an existing array and creating a new array out of then)
var4=np.array(["f","t","a","r","c","y"])
print("array: ",var4)
f=[True,False,True,True,False,False]
new_var4=var4[f]
print("Filtered array: ",new_var4)
print(type(new_var4))
print()

# Lecture 16
# Numpy array functions(shuffle,unique,resize,flatten,ravel)
# 1. Shuffle
import numpy as np
var=np.array([3,4,5,6,7])
print("array: ",var)
np.random.shuffle(var)
print("shuffled array: ",var)
# 2. Unique
var=np.array([3,4,3,5,4,6,5,1,1,7])
print("array: ",var)
x=np.unique(var) #it will return unique values.
print("unique element of array: ",x)
print()
x1=np.unique(var,return_index=True)
print("index of unique element: ",x1)
print()
x2=np.unique(var,return_counts=True)
print("count repitition of unique element: ",x2)
print()
# 3.Resize
var1=np.array([3,4,3,5,4,6,5,1,1])
print("array: ",)
x=np.resize(var1,(3,3))
print("Resized array: ",x)
print()
# 4. Flatten(convert nD array into 1D array)
var1=np.array([[3,4,3],[5,4,6],[5,1,1]])
print("array: ",var1)
print("flattened array: ",var1.flatten()) # it will convert nD array into 1D array.
print("flattened array in C-style(row): ",var1.flatten(order="C")) # "C" means to flatten in row major(C-style) order.
print("flattened array in fortan style(column) : ",var1.flatten(order="F")) #"F" means to flatten in coumn major(fortan style) order 
print()
# 5. Ravel(converts nD array into 1D array)
var2=np.array([[3,4,3],[5,4,6],[5,1,1]])
print("array: ",var2)
print("Ravel: ",np.ravel(var2))
print("Ravel order 'A': ",np.ravel(var2,order="A"))
print("Ravel order 'F': ",np.ravel(var2,order="F"))
print("Ravel order 'K': ",np.ravel(var2,order="K"))
print("Ravel order 'C': ",np.ravel(var2,order="C"))
print()

# Lecture 17
# Numpy insert and delete arrays function.
# 1. for 1D array. 
import numpy as np
var=np.array([4,5,8,2,5])
print("1D array: ",var)
v1=np.insert(var,3,50) # insert(arrayname,position,value)
v2=np.insert(var,(3,4),50)
v3=np.insert(var,(3,4),8.9) #it will not accept float value.
print("insert 50 in the array: ",v1)
print("insert 50 in the array: ",v2)
print("insert 8.9 in the array: ",v3)
print("it will not accept float value")
print()
# for 2D array. 
var_2=np.array([[3,4,5],[7,3,8]])
v4=np.insert(var_2,2,10,axis=0) # insert(arrayname,position,value,axis)
v5=np.insert(var_2,2,10,axis=1) 
v6=np.insert(var_2,2,[10,6],axis=1)# insert multiple values.
v7=np.insert(var_2,2,[10,5,8],axis=0) 
print("2D array:",var_2)
print("insert value in 2D array along axis=0:",v4)
print("insert value in 2D array along axis=1:",v5)
print("insert multiple value in 2D array along axis=1:",v6)
print("insert multiple value in 2D array along axis=1:",v7)
print()
# insert data through append function.
# for 1D array.
var=np.array([4,5,8,2,5])
print("1D array: ",var)
x=np.append(var,6.5)
print("append value in 1D array: ",x)
print()
# for 2D array.
var_2=np.array([[3,4,5],[7,3,8]])
print("2D array:",var_2)
x1=np.append(var_2,[[65,78,43]],axis=0)
print("append multiple value in 1D array: ",x1)
print()
# Delete function.
# for 1D array.
var=np.array([4,5,8,2,5])
print("1D array: ",var)
d=np.delete(var,2)
print("delete perticular value from array:",d)

print()

# Lecture 18.
# Concept of matrix in numpy arrays in python.
import numpy as np
var=np.matrix([[1,2,3],[4,5,6]])
print("matrix: ",var)
print(type(var))
print()

var1=np.array([[1,2,3],[4,5,6]])
print("array: ",var1)
print(type(var1))
print()

var_1=np.matrix([[1,2],[4,5]])
var_2=np.matrix([[7,9],[3,7]])
print("first matrix: ",var_1)
print("second matrix: ",var_2)
print("addition of matrices: ",var_1+var_2) # addition of matrix
print("multiplication of matrices: ",var_1*var_2) # multiplication of matrix
# Matrix function in numpy array
# 1. Transpose
import numpy as np
var=np.matrix([[1,2,3],[4,5,6]])
print("matrix: ",var)
print("Transpose of matrix: ",np.transpose(var))
# 2. Swapaxes(same as transport)
import numpy as np
var = np.matrix([[1,2],[4,5]])
print("matrix:", var)
print("swapaxes of matrix:", np.swapaxes(var, 0, 1))
print()

var2 = np.matrix([[1,2],[3,4]])
print(var2)
print("swapaxes of matrix:", np.swapaxes(var2, 0, 1))

# 3. Inverse matrix
var = np.matrix([[2,3],[5,6]])
print("matrix:", var)
print("inverse of matrix:", np.linalg.inv(var))
print()
# 4. Power (np.linalg.matrix_power(matrixname,n)) where n<0(inverse*power),n>0(power multiply),n=0(identity matrix)
var = np.matrix([[2,3],[5,6]])
print("matrix:", var)
print("power of matrix when n>0: ",np.linalg.matrix_power(var,2)) # n>0
print("power of matrix when n=0: ",np.linalg.matrix_power(var,0)) # n=0
print("power of matrix when n<0: ",np.linalg.matrix_power(var,-2)) #n<0
print()
# 5.Determinant(np.linalg.det(matrixname))
var = np.matrix([[2,3,4],[5,6,9],[1,5,3]])
print("matrix:", var)
print("determinant of matrix: ",np.linalg.det(var))





