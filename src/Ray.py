import math
from Vec3 import Vector


class Ray:
    def __init__(self, origin: Vector=None, direction: Vector=None):
        self.origin, self.direction = origin, direction

    def __str__(self):
        return f"Origin: {self.origin}, Direction: {self.direction}"

    def reflected_ray(self, origin, normal):
        direction = 2 * normal * \
            normal.dot_product(-self.direction) + self.direction
        return Ray(origin, direction)
