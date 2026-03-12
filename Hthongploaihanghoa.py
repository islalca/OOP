class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx

    def xuat_thong_tin(self):
        return f"Mã: {self.ma_hang} | Tên: {self.ten_hang} | NSX: {self.nha_sx}"

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.gia = gia
        self.bao_hanh = bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def xuat_thong_tin(self):
        base_info = super().xuat_thong_tin()
        return f"[Điện Máy] {base_info} | Giá: {self.gia:,.0f}đ | BH: {self.bao_hanh} tháng | Điện áp: {self.dien_ap}V | Công suất: {self.cong_suat}W"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.gia = gia
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def xuat_thong_tin(self):
        base_info = super().xuat_thong_tin()
        return f"[Sành Sứ] {base_info} | Giá: {self.gia:,.0f}đ | Nguyên liệu: {self.loai_nguyen_lieu}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hh):
        super().__init__(ma_hang, ten_hang, nha_sx)
        self.gia = gia
        self.ngay_sx = ngay_sx
        self.ngay_hh = ngay_hh

    def xuat_thong_tin(self):
        base_info = super().xuat_thong_tin()
        return f"[Thực Phẩm] {base_info} | Giá: {self.gia:,.0f}đ | NSX: {self.ngay_sx} | HSD: {self.ngay_hh}"

print("--- BT1: HÀNG HÓA ---")
tv = HangDienMay("DM01", "Tivi Sony 55 inch", "Sony", 15000000, 24, 220, 150)
binh_hoa = HangSanhSu("SS01", "Bình hoa Bát Tràng", "Bát Tràng", 500000, "Đất sét trắng")
sua = HangThucPham("TP01", "Sữa tươi Vinamilk", "Vinamilk", 35000, "01/04/2026", "01/10/2026")

print(tv.xuat_thong_tin())
print(binh_hoa.xuat_thong_tin())
print(sua.xuat_thong_tin())