import typing
from math import acos, sqrt
import numpy as np
from create_matrix import create_matrix


class Vector:
    def __init__(self, x: float=None, y: float=None, z: float=None):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __div__(self, scalar: float):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __truediv__(self, scalar: float):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rsub__(self, scalar):
        return Vector(scalar - self.x, scalar - self.y, scalar - self.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def magnitude(self):
        return sqrt(self.dot_product(self))

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def normal(self):
        magnitude = self.magnitude()
        return self if magnitude == 0 else self / magnitude

    def move(self, tx, ty, tz, direction):
        self.x += direction * tx
        self.y += direction * ty
        self.z += direction * tz

    def rotate_around_point(self, point, angle, axis, direction):
        self.move(point.x, point.y, point.z, -1)
        rotate_matrix = create_matrix(
            mat_type='rotation',
            angle=angle,
            axis=axis,
            direction=direction
        )
        result_vector = np.dot(rotate_matrix, self.vector())
        self.update_coords_from_vector(result_vector)
        self.move(point.x, point.y, point.z, 1)

    def vector(self):
        return np.array([self.x, self.y, self.z, 1])

    def update_coords_from_vector(self, vector):
        self.x, self.y, self.z = vector[0:3]

    def normalize(self):
        self = self.normal()

    def reflect_about_vector(self, other):
        '''Reflect this vector about another vector, returning a new vector as the result.'''
        return self - (other.normal() * (2 * self.dot_product(other)))
