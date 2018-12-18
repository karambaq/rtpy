from Vec3 import Vector
from Triangle import Triangle


def create_room(side, center, surfaces):
    s = side
    x, y, z = center.x, center.y, center.z

    p1 = Vector(x - s, y - s, z + s)  # left-bottom-far
    p2 = Vector(x - s, y + s, z + s)  # left-top-far
    p3 = Vector(x + s, y - s, z + s)  # right-bottom-far
    p4 = Vector(x + s, y + s, z + s)  # right-top-far
    p5 = Vector(x + s, y + s, z - s)  # right-top-near
    p6 = Vector(x + s, y - s, z - s)  # right-bottom-near
    p7 = Vector(x - s, y + s, z - s)  # left-top-near
    p8 = Vector(x - s, y - s, z - s)  # left-bottom-near

    # back
    b1 = Triangle([p1, p2, p3], surface=surfaces[0])
    b2 = Triangle([p2, p4, p3], surface=surfaces[0])
    # right
    r1 = Triangle([p4, p5, p3], surface=surfaces[1])
    r2 = Triangle([p6, p3, p5], surface=surfaces[1])
    # left
    l1 = Triangle([p2, p1, p7], surface=surfaces[2])
    l2 = Triangle([p7, p1, p8], surface=surfaces[2])
    # floor
    f1 = Triangle([p1, p6, p8], surface=surfaces[3])
    f2 = Triangle([p1, p3, p6], surface=surfaces[3])
    # ceil
    c1 = Triangle([p2, p7, p5], surface=surfaces[4])
    c2 = Triangle([p2, p5, p4], surface=surfaces[4])

    return [
        b1, b2,
        l1, l2,
        r1, r2,
        f1, f2,
        c1, c2
    ]


def build_cube(side, center, surfaces):
    h = side
    xc, yc, zc = center.x, center.y, center.z
    p1 = Vector(xc - h, yc - h, zc - h)
    p2 = Vector(xc + h, yc - h, zc - h)
    p3 = Vector(xc + h, yc - h, zc + h)
    p4 = Vector(xc - h, yc - h, zc + h)
    p5 = Vector(xc - h, yc + h, zc - h)
    p6 = Vector(xc + h, yc + h, zc - h)
    p7 = Vector(xc + h, yc + h, zc + h)
    p8 = Vector(xc - h, yc + h, zc + h)
    f11 = Triangle([p5, p1, p8], surface=surfaces[0])
    f12 = Triangle([p1, p4, p8], surface=surfaces[0])
    f21 = Triangle([p6, p2, p5], surface=surfaces[0])
    f22 = Triangle([p2, p1, p5], surface=surfaces[0])
    f31 = Triangle([p7, p3, p6], surface=surfaces[0])
    f32 = Triangle([p3, p2, p6], surface=surfaces[0])
    f41 = Triangle([p8, p4, p7], surface=surfaces[0])
    f42 = Triangle([p4, p3, p7], surface=surfaces[0])
    f51 = Triangle([p5, p8, p6], surface=surfaces[0])
    f52 = Triangle([p8, p7, p6], surface=surfaces[0])
    f61 = Triangle([p4, p1, p3], surface=surfaces[0])
    f62 = Triangle([p1, p2, p3], surface=surfaces[0])

    return [
        f11, f12,
        f21, f22,
        f31, f32,
        f41, f42,
        f51, f52,
        f61, f62,
    ]
