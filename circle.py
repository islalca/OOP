import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner 
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def point_in_circle(circle, point):
    khoang_cach = math.sqrt((circle.center.x - point.x)**2 + (circle.center.y - point.y)**2)
    return khoang_cach <= circle.radius

def rect_in_circle(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    
    return (point_in_circle(circle, p1) and point_in_circle(circle, p2) and 
            point_in_circle(circle, p3) and point_in_circle(circle, p4))

def rect_circle_overlap(circle, rect):
    closest_x = max(rect.corner.x, min(circle.center.x, rect.corner.x + rect.width))
    closest_y = max(rect.corner.y, min(circle.center.y, rect.corner.y + rect.height))

    distance_x = circle.center.x - closest_x
    distance_y = circle.center.y - closest_y

    return (distance_x**2 + distance_y**2) <= (circle.radius**2)