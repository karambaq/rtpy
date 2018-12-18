import numpy as np
from math import pow
from Vec3 import Vector
from Ray import Ray
from Color import Color

FARAWAY = 1e30


class Raytracer:
    def __init__(self, scene):
        self.scene = scene

    def trace_ray(self, ray, near, far, depth):
        nearest_obj, nearest = self.closest_intersection(ray, near, far)
        if not nearest_obj:
            return Color(0., 0., 0.)

        # nearest - distance to nearest object
        # here we compute the actual point of intersection
        intersection_point = ray.origin + ray.direction * nearest
        norm = nearest_obj.normal(intersection_point)

        light = self.compute_light(
            intersection_point, norm, -ray.direction, nearest_obj.surface)
        local_color = nearest_obj.surface.color * light

        # If recursion level is zero or object is not reflective, we're done
        r = nearest_obj.surface.reflective
        if depth <= 0 or r <= 0:
            return local_color

        # Compute reflective color
        reflected_ray = ray.reflected_ray(intersection_point, norm)
        reflected_color = self.trace_ray(
            Ray(intersection_point, reflected_ray.direction), 0.001, FARAWAY, depth - 1)

        return (1 - nearest_obj.surface.reflective) * local_color + \
            nearest_obj.surface.reflective * reflected_color

    def closest_intersection(self, ray, near, far):
        nearest = FARAWAY
        nearest_obj = None
        for obj in self.scene.objects:
            d1, d2 = obj.intersect(ray)
            if near < d1 < far and d1 < nearest:
                nearest = d1
                nearest_obj = obj
            if near < d2 < far and d2 < nearest:
                nearest = d2
                nearest_obj = obj
        return nearest_obj, nearest

    def compute_light(self, point, normal, view, surface):
        intensity = 0
        for light in self.scene.lights:
            intensity += light.ambient
            to_light = light.position - point
            far = 1

            shadow_ray = Ray(point, to_light)
            shadow_obj, shadow_d = self.closest_intersection(
                shadow_ray, 0.001, far)
            if shadow_obj is not None:
                continue

            # Diffuse light
            intensity += compute_diffuse(normal, to_light, light)

            # Specular light
            intensity += compute_specular(normal,
                                          to_light, light, view, surface)

        return intensity


def compute_diffuse(normal, to_light, light):
    diffuse = 0
    n_dot_l = normal.dot_product(to_light)
    if n_dot_l > 0:
        diffuse += light.intensity * n_dot_l \
            / (normal.magnitude() * to_light.magnitude())
    return diffuse


def compute_specular(normal, to_light, light, view, surface):
    specular = 0
    if surface.specular != -1:
        vec_r = (2.0 * normal.dot_product(to_light)
                 * normal) - to_light
        r_dot_v = vec_r.dot_product(view)
        if r_dot_v > 0:
            specular += light.intensity * \
                pow(r_dot_v /
                    (vec_r.magnitude() * view.magnitude()),
                    surface.specular
                    )
    return specular
