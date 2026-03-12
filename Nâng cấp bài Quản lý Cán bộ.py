from abc import ABC, abstractmethod

# Custom Exception
class TuoiKhongHopLe(Exception): pass
class BacKhongHopLe(Exception): pass

# Abstract Class
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(f"Tuổi {value} không hợp lệ! (Phải từ 18-65)")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.ho_ten}, {self.tuoi} tuổi, {self.gioi_tinh}, {self.dia_chi}"

    def __repr__(self):
        # Trả về chuỗi để có thể khôi phục lại object
        return f"CanBo('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}')"

    def __eq__(self, other):
        if isinstance(other, CanBo):
            return self.ho_ten == other.ho_ten and self.tuoi == other.tuoi
        return False

    def __lt__(self, other):
        # Sắp xếp theo tên (lấy từ cuối cùng trong chuỗi họ tên)
        ten_self = self.ho_ten.split()[-1] if self.ho_ten else ""
        ten_other = other.ho_ten.split()[-1] if other.ho_ten else ""
        return ten_self < ten_other

# Lớp kế thừa
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    @property
    def bac(self):
        return self._bac
    
    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe("Bậc công nhân phải từ 1 đến 10")
        self._bac = value

    def mo_ta(self):
        return f"[Công Nhân - Bậc {self.bac}] {super().__str__()}"
        
    def __repr__(self):
        return f"CongNhan('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}', {self.bac})"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

    def mo_ta(self):
        return f"[Kỹ Sư - Ngành: {self.nganh}] {super().__str__()}"
        
    def __repr__(self):
        return f"KySu('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}', '{self.nganh}')"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"[Nhân Viên - CV: {self.cong_viec}] {super().__str__()}"

    def __repr__(self):
        return f"NhanVien('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}', '{self.cong_viec}')"


if __name__ == "__main__":
    # Ví dụ đa hình
    ds_canbo = [
        CongNhan("Nguyen Van A", 30, "Nam", "HN", 5),
        KySu("Tran Thi B", 28, "Nữ", "HCM", "CNTT"),
        NhanVien("Le Van C", 35, "Nam", "DN", "Kế toán")
    ]
    
    print("--- Danh sách cán bộ (Sắp xếp theo tên) ---")
    for cb in sorted(ds_canbo):
        print(cb.mo_ta())

    # Lưu file bằng context manager
    with open("canbo.txt", "w", encoding="utf-8") as f:
        for cb in ds_canbo:
            f.write(repr(cb) + "\n")