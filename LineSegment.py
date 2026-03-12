class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"

class LineSegment:
    def __init__(self, arg1=None, arg2=None):
        # 1. Constructor mặc định (không truyền đối số)
        if arg1 is None and arg2 is None:
            self.__d1 = Point(0, 0)
            self.__d2 = Point(0, 0)
            
        # 2. Constructor có 2 đối số là Point (Sao chép sâu - Deep Copy)
        elif isinstance(arg1, Point) and isinstance(arg2, Point):
            self.__d1 = Point(arg1.x, arg1.y) # Tạo điểm mới hoàn toàn
            self.__d2 = Point(arg2.x, arg2.y)
            
        # 3. Constructor có đối số (Point, int) như ghi chú trong đề
        # Giả sử int là độ dài của đoạn thẳng chạy ngang trên trục X
        elif isinstance(arg1, Point) and isinstance(arg2, int):
            self.__d1 = Point(arg1.x, arg1.y)
            self.__d2 = Point(arg1.x + arg2, arg1.y)

    # --- GETTER / SETTER ---
    def get_d1(self):
        return self.__d1
        
    def set_d1(self, p):
        # Luôn phải sao chép sâu khi set
        self.__d1 = Point(p.x, p.y)

    def get_d2(self):
        return self.__d2
        
    def set_d2(self, p):
        self.__d2 = Point(p.x, p.y)

    def in_thong_tin(self):
        print(f"Đoạn thẳng nối 2 điểm: d1{self.__d1} và d2{self.__d2}")

# --- CHẠY THỬ BÀI 2 ---
print("\n--- TEST LỚP LINESEGMENT ---")
# Test Constructor (Point, Point) với sao chép sâu
pA = Point(2, 3)
pB = Point(5, 7)
doan_thang_1 = LineSegment(pA, pB)
doan_thang_1.in_thong_tin()

# Chứng minh sao chép sâu: Thay đổi pA ở ngoài không làm ảnh hưởng d1 bên trong
pA.x = 999 
print("Sau khi đổi tọa độ pA bên ngoài:")
doan_thang_1.in_thong_tin() # Tọa độ d1 vẫn giữ nguyên là (2, 3)

# Test Constructor (Point, int) như trong ảnh
pC = Point(0, 0)
doan_thang_2 = LineSegment(pC, 10) # Độ dài 10
print("Test Constructor (Point, int):")
doan_thang_2.in_thong_tin()