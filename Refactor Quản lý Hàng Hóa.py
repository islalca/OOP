from abc import ABC, abstractmethod

# 1. Custom Exceptions
class GiaKhongHopLe(Exception):
    pass

class MaHangTrungLap(Exception):
    pass

# 2. Abstract Base Class
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.gia = gia  # Gọi setter để kiểm tra dữ liệu

    # @property cho các thuộc tính read-only
    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    # @property + setter (validation)
    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(f"Giá không hợp lệ ({value}). Giá phải >= 0.")
        self._gia = value

    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    # Magic Methods
    def __str__(self):
        return f"Mã: {self.ma_hang} | Tên: {self.ten_hang} | Giá: {self.gia}"

    def __eq__(self, other):
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False

    def __lt__(self, other):
        return self.gia < other.gia

    def __hash__(self):
        return hash(self.ma_hang)

# 3. Các lớp kế thừa
class HangDienMay(HangHoa):
    def loai_hang(self):
        return "Hàng Điện Máy"

    def inTTin(self):
        return f"[{self.loai_hang()}] {super().__str__()}"

class HangSanhSu(HangHoa):
    def loai_hang(self):
        return "Hàng Sành Sứ"

    def inTTin(self):
        return f"[{self.loai_hang()}] {super().__str__()}"

class HangThucPham(HangHoa):
    def loai_hang(self):
        return "Hàng Thực Phẩm"

    def inTTin(self):
        return f"[{self.loai_hang()}] {super().__str__()}"

# 4. Demo Context Manager (lưu/đọc danh sách từ file)
if __name__ == "__main__":
    danh_sach = {
        HangDienMay("DM01", "Tủ Lạnh", 15000),
        HangSanhSu("SS01", "Chén sứ", 50),
        HangThucPham("TP01", "Thịt bò", 300)
    }
    
    # Sắp xếp theo giá (dùng __lt__)
    ds_sorted = sorted(danh_sach)
    
    print("Danh sách hàng hóa (đã sắp xếp theo giá):")
    for sp in ds_sorted:
        print(sp.inTTin()) # Đa hình

    # Lưu file
    with open("hanghoa.txt", "w", encoding="utf-8") as f:
        for sp in ds_sorted:
            f.write(sp.inTTin() + "\n")