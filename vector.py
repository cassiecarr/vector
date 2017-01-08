import math
from decimal import Decimal, getcontext

##This library is a set of functions for doing basic linear algebra
##functions with vectors

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        add_vector = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(add_vector)

    def subtract(self, v):
        sub_vector = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(sub_vector)

    def scalar(self, scale):
        scale_vector = [scale*x for x in self.coordinates]
        return Vector(scale_vector)

    def magnitude(self):
        x=Decimal(0.0)
        n=len(self.coordinates)
        for i in range(n):
            x=x+Decimal(math.pow(self.coordinates[i],2))
        x=math.sqrt(x)
        return x

    def normalize(self):
        try:
            mag = Decimal(Vector.magnitude(self))
            inv_mag = Decimal('1.0')/mag
            return Vector.scalar(self, inv_mag)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, v):
        x=Decimal(0.0)
        n=len(self.coordinates)
        for i in range(n):
            x=x+(self.coordinates[i]*v.coordinates[i])
        return x

    def angle(self,v,in_degrees=False):
        try:
            u1 = self.normalize()
            u2 = v.normalize()
            x=math.acos(round(u1.dot_product(u2),6))
            if in_degrees:
                return math.degrees(x)
            else:
                return x
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def is_zero(self):
        return self.magnitude() < 1e-10

    def is_parallel(self,v):
        ang = 0
        if not (self.is_zero() or v.is_zero()):
            ang = self.angle(v)
        return (self.is_zero() or v.is_zero() or ang==0 or ang==math.pi)

    def is_orthagonal(self,v):
        return abs(self.dot_product(v)) < 1e-10

    def projection(self,b):
        unit_vector_b = b.normalize()
        return Vector.scalar(unit_vector_b,Vector.dot_product(self,unit_vector_b))

    def orthogonal(self,b):
        vector_parallel = Vector.projection(self,b)
        vector_orthogonal = Vector.subtract(self,vector_parallel)
        return vector_orthogonal

    def cross_product(self,w):
        x_1,y_1,z_1 = self.coordinates
        x_2,y_2,z_2 = w.coordinates
        new_coordinates = [y_1*z_2 - y_2*z_1,
                           -(x_1*z_2 - x_2*z_1),
                           x_1*y_2 - x_2*y_1]
        return Vector(new_coordinates)

    def area_parallelogram(self,w):
        return Vector.magnitude(Vector.cross_product(self,w))

    def area_triangle(self,w):
        return 0.5*Vector.area_parallelogram(self,w)

