from numpy import clip


class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def components(self):
        return clip((self.r * 255.0, self.g * 255.0, self.b * 255.0), 0, 255)

    def __mul__(self, scalar):
        return Color(self.r * scalar, self.g * scalar, self.b * scalar)

    def __rmul__(self, scalar):
        return Color(self.r * scalar, self.g * scalar, self.b * scalar)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)
