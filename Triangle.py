import numpy as np
import math
from Vec3 import Vector
from Ray import Ray
from Math import solve_quadratic
from create_matrix import create_matrix

FARAWAY = 1e30


class Triangle:
    def __init__(self, verteces, surface=None, norm=None):
        self.verteces = verteces
        self.surface = surface
        self.norm = norm

    def __str__(self):
        t = ""
        for v in self.verteces:
            t += str(v) + "\n"
        return t

    def __repr__(self):
        t = ""
        for v in self.verteces:
            t += str(v) + "\n"
        return t + "\n"

    def normal(self, at: Vector):
        if self.norm:
            return self.norm
        v0, v1, v2 = self.verteces
        v0v1 = v1 - v0
        v0v2 = v2 - v0

        pvec = v0v1.cross_product(v0v2)
        return pvec.normal()

    def intersect(self, ray: Ray):
        """
            https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm
        """
        v0, v1, v2 = self.verteces
        v0v1 = v1 - v0
        v0v2 = v2 - v0
        pvec = ray.direction.cross_product(v0v2)

        det = v0v1.dot_product(pvec)

        if det < 0.000001:
            return FARAWAY, FARAWAY

        invDet = 1.0 / det
        tvec = ray.origin - v0
        u = tvec.dot_product(pvec) * invDet

        if u < 0 or u > 1:
            return FARAWAY, FARAWAY

        qvec = tvec.cross_product(v0v1)
        v = ray.direction.dot_product(qvec) * invDet

        if v < 0 or u + v > 1:
            return FARAWAY, FARAWAY
        hit = v0v2.dot_product(qvec) * invDet

        return hit, hit

    def rotate(self, point, x=None, y=None, z=None, rotated=None):
        for vertex in self.verteces:
            if str(hash(vertex)) not in rotated:
                if x:
                    vertex.rotate_around_point(point, x * np.pi / 180, 'x', 1)
                if y:
                    vertex.rotate_around_point(point, y * np.pi / 180, 'y', 1)
                if z:
                    vertex.rotate_around_point(point, z * np.pi / 180, 'z', 1)
                rotated.append(str(hash(vertex)))
