from math import sqrt

FARAWAY = 1e30


def solve_quadratic(a, b, c):
    d = b * b - 4 * a * c
    if d >= 0:
        d_sqrt = sqrt(d)
        a_sqr = 2 * a
        r1 = (-b + d_sqrt) / (a_sqr)
        r2 = (-b - d_sqrt) / (a_sqr)
        return r1, r2
    return FARAWAY, FARAWAY
