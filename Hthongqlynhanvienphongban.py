class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = max(0.1, he_so_luong) # Đảm bảo hệ số lương > 0
        self.luong_toi_da = luong_toi_da

    def xuat_thong_tin_chung(self):
        return f"Mã: {self.ma_nv} | Tên: {self.ho_ten} | Hệ số: {self.he_so_luong}"

class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap = phu_cap
        
    def thu_nhap(self):
        # Giả sử lương cơ sở là 1,500,000đ
        luong_cb = 1500000 
        tong = (luong_cb * self.he_so_luong) + self.phu_cap
        return min(tong, self.luong_toi_da)

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri = vi_tri

    def tinh_luong(self):
        luong_cb = 1500000
        tong = luong_cb * self.he_so_luong
        return min(tong, self.luong_toi_da)

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau_ql, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bat_dau_ql = ngay_bat_dau_ql
        self.phu_cap_ql = phu_cap_ql

    def thu_nhap(self):
        luong_cb = 1500000
        tong = (luong_cb * self.he_so_luong) + self.phu_cap_ql
        return min(tong, self.luong_toi_da)

print("\n--- BT2: NHÂN VIÊN PHÒNG BAN ---")
ctv = CongTacVien("CTV01", "Nguyễn Văn A", 2000, "Nam", "HN", 1.5, 10000000, "6 tháng", 500000)
print(f"[CTV] {ctv.xuat_thong_tin_chung()} | Thu nhập: {ctv.thu_nhap():,.0f}đ")