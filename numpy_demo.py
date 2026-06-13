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

