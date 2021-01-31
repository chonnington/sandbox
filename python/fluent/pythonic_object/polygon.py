import math


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]] # close the "loop"
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter

square = [(1,1), (1,2), (2,2), (2,1)]
print(perimeter(square))


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)


class Polygon:

    def __init__(self, vertices=None):

        if vertices is None:
            self.vertices = []
        else:
            self.vertices = vertices

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


square = Polygon()

square.add_point(Point(1,1))
square.add_point(Point(1,2))
square.add_point(Point(2,2))
square.add_point(Point(2,1))

print(square.perimeter())

del square

square = Polygon([Point(1,1), Point(1,2), Point(2,2), Point(2,1)])
print(square.perimeter())

