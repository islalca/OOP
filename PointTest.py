import math

class PointTest:
    @staticmethod
    def main():
        a = Point(3, 4)
        print("Tọa độ điểm A:", end=" ")
        a.print()

        b = Point()
        print("Nhập tọa độ cho điểm B (x y):")
        b.read()
        print("Tọa độ điểm B:", end=" ")
        b.print()


        c = Point(-b.getX(), -b.getY())
        print("Tọa độ điểm C (đối xứng với B qua gốc tọa độ):", end=" ")
        c.print()

        dist_b_o = b.distance()
        print(f"Khoảng cách từ B đến gốc tọa độ: {dist_b_o}")

        dist_a_b = a.distance(b)
        print(f"Khoảng cách từ A đến B: {dist_a_b}")