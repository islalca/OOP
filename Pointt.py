import math

class Point:

    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        try:
            data = input().split()
            if len(data) >= 2:
                self.__x = int(data[0])
                self.__y = int(data[1])
        except ValueError:
            pass
    def print(self):
        print(f"({self.__x}, {self.__y})")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    def distance(self, p=None):
        if p is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            dx = self.__x - p.getX()
            dy = self.__y - p.getY()
            return math.sqrt(dx**2 + dy**2)