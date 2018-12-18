import numpy as np
from PIL import Image
import time

from Color import Color
from Ray import Ray
from Scene import Scene
from Sphere import Sphere
from Surface import *
from Vec3 import Vector
from Light import Light
from Triangle import Triangle
from Raytracer import Raytracer
from Cube import create_room, build_cube


FARAWAY = 1e30
WIDTH = 200
HEIGHT = 200
DEPTH = 3


room = create_room(1, Vector(0, 0, 3), surfaces=[
                   grey_specular, green_wall, red_wall, grey_specular, grey_specular]),

small_cube = build_cube(.25, Vector(-.5, -.76, 3.2), surfaces=[grey])
rotated = []
for triangle in small_cube:
    triangle.rotate(Vector(-.5, -.76, 2.0), x=-5, y=10, rotated=rotated)

# mirror
x, y, z = 0, 0, 3
s = 0.8
p3 = Vector(x + .98, y - .85, z + s / 2)  # right-bottom
p4 = Vector(x + .98, y + .85, z + s / 2)  # right-top
p5 = Vector(x + .98, y + .85, z - s)  # left-top
p6 = Vector(x + .98, y - .85, z - s)  # right-bottom
r1 = Triangle([p4, p5, p3], surface=mirror)
r2 = Triangle([p6, p3, p5], surface=mirror)

scene = Scene(
    camera=Vector(0, 0, 0),
    width=WIDTH,
    height=HEIGHT,
    objects=[
        Sphere(Vector(.5, -0.7, 3.2), 0.3, surface=silver),
        # mirror
        r1, r2,
        # mandarine
        Sphere(Vector(0, -0.8, 2.2), 0.2, surface=orange),
        Sphere(Vector(-0.05, -0.625, 2.1), 0.022, surface=green_wall),

        # light
        Triangle(
            [
                Vector(-0.25, 0.98, 2.7),  # right-bottom
                Vector(-0.25, 0.98, 2.3),  # left-top
                Vector(0.25, 0.98, 2.3),  # left-bottom
            ],
            surface=light_surface
        ),
        Triangle(
            [
                Vector(-0.25, 0.98, 2.7),  # right-bottom
                Vector(0.25, 0.98, 2.3),  # left-bottom
                Vector(0.25, 0.98, 2.7),  # left-top
            ],
            surface=light_surface
        ),
        *room[0],
        *small_cube,
    ],
    lights=[
        Light(ambient=0.25, intensity=0.6,
              position=Vector(0.001, 0.80, 2.75)),
        Light(ambient=0, intensity=0.2,
              position=Vector(-0.4, 0.80, 1.5)),
    ]
)

data = np.zeros((HEIGHT, WIDTH, 3))
camera = scene.camera
raytracer = Raytracer(scene)

start = time.time()
for i, x in enumerate(np.linspace(-0.5, 0.5, WIDTH)):
    print(f"{round(x * 100 + 50, 2)}%")
    for j, y in enumerate(np.linspace(-0.5, 0.5, HEIGHT + 1)):
        primary_ray = Ray(
            camera, (Vector(x, y, 1) - camera))
        color = raytracer.trace_ray(primary_ray, 1.0, FARAWAY, DEPTH)
        data[-j, i] = color.components()
print(time.time() - start)

img = Image.fromarray(data.astype('uint8'), 'RGB')
img.save('img.png')
