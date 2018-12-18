
class Scene:
    def __init__(self, camera, width, height, objects, lights, fov=60):
        self.camera = camera
        self.width = width
        self.height = height
        self.objects = objects
        self.lights = lights
        self.fov = fov
