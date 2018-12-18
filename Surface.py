from Color import Color

GREEN = Color(0, 1., 0)
RED = Color(1., 0, 0)
BLUE = Color(0, 0, 1.)
YELLOW = Color(1., 1., 0)


class Surface:
    def __init__(self, color=None, specular=None, diffuse=None, ambient=None, reflective=None):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflective = reflective


red_specular = Surface(color=RED, specular=500, reflective=0.2)
blue_specular = Surface(color=BLUE, specular=10, reflective=0.0)
orange = Surface(color=Color(.94, .52, 0), specular=10, reflective=0.0)
silver = Surface(color=Color(.7, .7, .7), specular=500, reflective=0.8)
yellow_specular = Surface(color=YELLOW, specular=1000, reflective=1.0)
yellow = Surface(color=YELLOW, specular=10, reflective=0.0)
grey = Surface(color=Color(.9, .9, .9), specular=10, reflective=0.0)

# walls
red_wall = Surface(color=Color(.62, .2, .2), specular=10, reflective=-1)
green_wall = Surface(color=Color(.2, .52, .2), specular=10, reflective=-1)
#green_wall = Surface(color=Color(.0, .99, .0), specular=10, reflective=0.)
blue_wall = Surface(color=BLUE, specular=50, reflective=0.0)
grey_specular = Surface(color=Color(.6, .6, .6), specular=10, reflective=0.0)

# light
light_surface = Surface(color=Color(1., 1., 1.), specular=0, reflective=-1)
mirror = Surface(color=Color(1., 1., 1.), specular=-10, reflective=1.0)
