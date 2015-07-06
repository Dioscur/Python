import math
class Sphere(object):

    def __init__ (self, r=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = r
        self.center = (x,y,z)

    def get_volume(self):
        return 4.0*math.pi*(self.radius**3)/3

    def get_square(self):
        return 4.0*math.pi*self.radius**2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.center[0]*1.0,self.center[1]*1.0,self.center[2]*1.0)

    def set_radius(self,r):
        self.radius = r * 1.0

    def set_center(self, x=0, y=0, z=0):
        self.center = (x,y,z)

    def is_point_inside(self, x,y,z):
        dist = math.sqrt((self.center[0]-x)**2 + (self.center[1]-y)**2 + (self.center[2]-z)**2)
        return self.radius > dist

s0 = Sphere (0.5, 1.0, 0.0,0.0)
print s0.get_center()
print s0.get_volume()
print s0.is_point_inside(0, -1.5, 0)
s0.set_radius(1.6)
print s0.is_point_inside(0, -1.5, 0)
print s0.get_radius()
s1 = Sphere (1, 2,2,2)
s1.set_radius(2)
print s1.get_radius()
print s1.get_center()
