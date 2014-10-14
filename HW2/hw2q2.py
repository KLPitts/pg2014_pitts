import matplotlib.pyplot as plt
from math import sqrt, sin, cos, pi

class Point(object):
    """Class that adds, subtracts, rotates, and calculates distances 
    between points.
    
	Author
	___________
	Katie Pitts
	Oct 14, 2014
	KLPitts@tamu.edu
    
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        """Method that adds point to other point"""
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        """Method that subtracts other point from point"""
        return Point(self.x-other.x, self.y-other.y)
        
    def rotate(self, radians, p=None):
        """Method that rotates point around Point(p).
        Default Point(p) is (0.0,0.0)."""
        if p is None:
            p = Point(0.0, 0.0)

        new = self - p
        RotX = (new.x * cos(-radians)) - (new.y * sin(-radians))
        RotY = (new.x * sin(-radians)) + (new.y * cos(-radians))
        NewPoint = (RotX + p.x, RotY + p.y)
        self.x = NewPoint[0]
        self.y = NewPoint[1]

    def distance(self, p=None):
        """Method that calculates distance between point and Point(p).
        Default Point(p) is (0.0,0.0)."""
        if p is None:
            p = Point(0.0, 0.0)
        return sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )

if __name__ == '__main__':
	p1 = Point(3.0, 4.0)
	print 'Original point: (%f, %f)' % (p1.x, p1.y)
	plt.plot(p1.x,p1.y,'bo', label='Original point')
	origin = Point(2.0,-1.0)
	plt.plot(origin.x,origin.y,'ko', label='Origin point')
	print 'Origin point: (%f, %f)' % (origin.x, origin.y)
	radians=3*pi/2
	p1.rotate(radians=radians, p=origin)
	print 'Rotate Original point clockwise around Origin point by %f radians' % (radians)
	print 'Rotated point: (%f, %f)' % (p1.x, p1.y)
	plt.plot(p1.x,p1.y,'ro',label='Rotated point')
	plt.xlim([-5,5])
	plt.ylim([-5,5])
	plt.grid('on')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend(loc='best')
	plt.show()