# vector

This vector class was built using the Udacity linear algebra course.
It provides basic functions for doing vector mathematics

## Installation

Import the class, along with math and Decimal
Also, you will need to indicate your decimal precision

```python
from vector import Vector
import math
from decimal import Decimal, getcontext
getcontext().prec = 30
```

## Examples

Here are some examples of various methods provided by the vector class
These can also be found in the vector_examples.py file
```python
##Print vector and vectors equal
print("Print Vector: ")
my_vector = Vector([1,2,3])
my_vector1 = Vector([2,2,2])
print(my_vector)
print("Are the vectors equal: ",my_vector == my_vector1)
print("")

##Vector addition
print('Addition Test:')
my_vector2 = Vector([8.218,-9.341])
my_vector3 = Vector([-1.129,2.111])
my_vector4 = Vector.plus(my_vector2,my_vector3)
print(my_vector4)
print("")

##Vector subtraction
print('Subtraction Test:')
my_vector2 = Vector([7.119,8.215])
my_vector3 = Vector([-8.223,0.878])
my_vector4 = Vector.subtract(my_vector2,my_vector3)
print(my_vector4)
print("")

##Vector scalar
print('Scalar Test:')
my_vector3 = Vector([1.671,-1.012,-0.318])
scale = Decimal(7.41)
my_vector4 = Vector.scalar(my_vector3,scale)
print(my_vector4)
print("")

##Vector magnitude
print('Vector Magnitude Test:')
my_vector = Vector([-0.221,7.437])
y = Vector.magnitude(my_vector)
print(y)
my_vector = Vector([8.813,-1.331,-6.247])
y = Vector.magnitude(my_vector)
print(y)
print("")

##Determine unit vector with normalize
print('Normalize Vector Test:')
my_vector = Vector([5.581,-2.136])
y = Vector.normalize(my_vector)
print(y)
my_vector = Vector([1.996,3.108,-4.554])
y = Vector.normalize(my_vector)
print(y)
print("")

##Dot Product of 2 vectors
print('Find Dot Product Test:')
my_vector = Vector([7.887,4.138])
my_vector2 = Vector([-8.802,6.776])
y = Vector.dot_product(my_vector,my_vector2)
print(y)
my_vector = Vector([-5.955,-4.904,-1.874])
my_vector2 = Vector([-4.496,-8.755,7.103])
y = Vector.dot_product(my_vector,my_vector2)
print(y)
print("")

##Angle between two vectors
print('Find Angle between Vectors Test:')
my_vector = Vector([3.183,-7.627])
my_vector2 = Vector([-2.668,5.319])
y = Vector.angle(my_vector,my_vector2)
print(y)
my_vector = Vector([7.35,0.221,5.188])
my_vector2 = Vector([2.751,8.259,3.985])
y = Vector.angle(my_vector,my_vector2)
print(math.degrees(y))
print("")

##Find if 2 vectors are Parallel and/or Orthagonal to one another
print('Find if parallel or orthagonal:')
v = Vector([-7.579,-7.88])
w = Vector([22.737, 23.64])
print("Item 1: ",v.is_parallel(w)," ",v.is_orthagonal(w))
v = Vector([-2.029,9.97,4.172])
w = Vector([-9.231,-6.639,-7.245])
print("Item 2: ",v.is_parallel(w)," ",v.is_orthagonal(w))
v = Vector([-2.328,-7.284,-1.214])
w = Vector([-1.821,1.072,-2.94])
print("Item 3: ",v.is_parallel(w)," ",v.is_orthagonal(w))
v = Vector([2.118,4.827])
w = Vector([0,0])
print("Item 4: ",v.is_parallel(w)," ",v.is_orthagonal(w))
print("")

##Projection of one vector onto another and finding the
##Parallel and Orthogonal components of the projection
print('Projection of v onto b: ')
v = Vector([3.039,1.879])
b = Vector([0.825,2.036])
v_parallel = Vector.projection(v,b)
print(v_parallel)
print("")
print('Orthogonal of v onto b: ')
v = Vector([-9.88,-3.264,-8.159])
b = Vector([-2.155,-9.353,-9.473])
v_orthogonal = Vector.orthogonal(v,b)
print(v_orthogonal)
print("")
print('Projection and orthogonal of v onto b: ')
v = Vector([3.009,-6.172,3.692,-2.51])
b = Vector([6.404,-9.144,2.759,8.718])
v_parallel = Vector.projection(v,b)
v_orthogonal = Vector.orthogonal(v,b)
print(v_parallel," + ",v_orthogonal)
print("")

##Vector Cross Product (3-Dimensional vectors only)
print('Cross Product of v and w: ')
v = Vector([8.462,7.893,-8.187])
w = Vector([6.984,-5.975,4.778])
print(Vector.cross_product(v,w))
print('Area of parallelogram made of v and w: ')
v = Vector([-8.987,-9.838,5.031])
w = Vector([-4.268,-1.861,-8.866])
print(Vector.area_parallelogram(v,w))
print('Area of triangle made of v and w: ')
v = Vector([1.5,9.547,3.691])
w = Vector([-6.007,0.124,5.772])
print(Vector.area_triangle(v,w))
```