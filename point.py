import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def hien_thi(self):
        print(f"({self.x}, {self.y})")

    def doi_xung_qua_O(self):
        return Point(-self.x, -self.y)

    def khoang_cach(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

print("--- BT 1 ---")
A = Point(3, 4)
print("Tọa độ điểm A:", end=" ")
A.hien_thi()

x_b = float(input("Nhập hoành độ x của B: "))
y_b = float(input("Nhập tung độ y của B: "))
B = Point(x_b, y_b)

C = B.doi_xung_qua_O()
print("Tọa độ điểm C (đối xứng B qua O):", end=" ")
C.hien_thi()

O = Point(0, 0) # Gốc tọa độ
print(f"Khoảng cách B -> O: {B.khoang_cach(O):.2f}")
print(f"Khoảng cách A -> B: {A.khoang_cach(B):.2f}")