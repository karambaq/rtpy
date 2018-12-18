import numpy as np
import math
from Vec3 import Vector
from Ray import Ray
from Math import solve_quadratic


class Sphere:
    def __init__(self, center: Vector, radius: float, surface=None):
        self.center = center
        self.radius = radius
        self.surface = surface

    def normal(self, at: Vector):
        """
            Returns normal vector of the sphere in point on the surface
        """
        return (at - self.center).normal()

    def intersect(self, ray: Ray):
        """
            Returns points of intersections of ray and sphere, 
            no intersections: returns FARAWAY, FARAWAY
            two intersections: returns distances from ray origin to points of intersections
        """
        oc = ray.origin - self.center
        a = ray.direction.dot_product(ray.direction)
        b = 2 * oc.dot_product(ray.direction)
        c = oc.dot_product(oc) - self.radius * self.radius
        return solve_quadratic(a, b, c)
