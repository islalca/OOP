import math

class MauSoBangKhong(Exception):
    pass

class PhanSo:
    def __init__(self, tu, mau):
        self.tu_so = tu
        self.mau_so = mau # Đi qua setter để check mẫu = 0

    @property
    def tu_so(self):
        return self._tu_so

    @tu_so.setter
    def tu_so(self, value):
        self._tu_so = value

    @property
    def mau_so(self):
        return self._mau_so

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong("Lỗi: Mẫu số không được bằng 0!")
        self._mau_so = value

    # Kiểm tra tối giản
    def is_toi_gian(self):
        return math.gcd(abs(self.tu_so), abs(self.mau_so)) == 1

    # Tìm dạng tối giản
    def toi_gian(self):
        ucln = math.gcd(abs(self.tu_so), abs(self.mau_so))
        tu_moi = self.tu_so // ucln
        mau_moi = self.mau_so // ucln
        # Đảm bảo mẫu số luôn dương để dễ nhìn (VD: 1/-2 -> -1/2)
        if mau_moi < 0:
            tu_moi = -tu_moi
            mau_moi = -mau_moi
        return PhanSo(tu_moi, mau_moi)

    # Magic Methods Tính Toán
    def __add__(self, other):
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        tu = self.tu_so * other.tu_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __truediv__(self, other):
        if other.tu_so == 0:
            raise MauSoBangKhong("Không thể chia cho phân số có tử số = 0")
        tu = self.tu_so * other.mau_so
        mau = self.mau_so * other.tu_so
        return PhanSo(tu, mau).toi_gian()

    # Magic Methods So Sánh
    def __eq__(self, other):
        ps1 = self.toi_gian()
        ps2 = other.toi_gian()
        return ps1.tu_so == ps2.tu_so and ps1.mau_so == ps2.mau_so

    def __lt__(self, other):
        return (self.tu_so * other.mau_so) < (other.tu_so * self.mau_so)

    def __gt__(self, other):
        return (self.tu_so * other.mau_so) > (other.tu_so * self.mau_so)

    # Hiển thị
    def __str__(self):
        ps = self.toi_gian()
        if ps.tu_so == 0:
            return "0"
        elif ps.mau_so == 1:
            return str(ps.tu_so)
        else:
            return f"{ps.tu_so}/{ps.mau_so}"

    def __repr__(self):
        return f"PhanSo({self.tu_so}, {self.mau_so})"

    def __hash__(self):
        ps = self.toi_gian()
        return hash((ps.tu_so, ps.mau_so))

# Viết chương trình ứng dụng
if __name__ == "__main__":
    # 1. Nhập một dãy các phân số (Cứng code để demo trực quan)
    ds_phan_so = [PhanSo(2, 4), PhanSo(5, 2), PhanSo(1, 2), PhanSo(-3, 6), PhanSo(4, 1)]
    
    # 2. In ra màn hình dạng tối giản (bản thân hàm __str__ đã gọi toi_gian)
    print("Danh sách phân số ban đầu (đã tối giản qua __str__):")
    print([str(ps) for ps in ds_phan_so])
    
    # 3. Sử dụng Set() để loại bỏ các phân số có cùng giá trị (vd 2/4 và 1/2) nhờ vào __hash__ và __eq__
    set_phan_so = set(ds_phan_so)
    print("\nDanh sách sau khi loại bỏ trùng giá trị (Set):")
    print([str(ps) for ps in set_phan_so])

    # 4. Sắp xếp dãy phân số tăng dần (sử dụng sorted nhờ vào __lt__)
    ds_sorted = sorted(set_phan_so)
    print("\nDanh sách phân số sau khi sắp xếp:")
    print([str(ps) for ps in ds_sorted])