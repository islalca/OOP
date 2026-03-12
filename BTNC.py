class NhanVienNC:
    # Hằng số quy định mức lương tối đa
    LUONG_MAX = 50000000 

    def __init__(self, ma_nv, ten_nv, luong_co_ban, he_so_luong):
        self._ma_nv = ma_nv
        self._ten_nv = ten_nv
        self._luong_co_ban = luong_co_ban
        self._he_so_luong = he_so_luong

    # --- Viết getter/setter cho tất cả thuộc tính bằng @property ---
    @property
    def ma_nv(self):
        return self._ma_nv

    @ma_nv.setter
    def ma_nv(self, value):
        self._ma_nv = value

    @property
    def ten_nv(self):
        return self._ten_nv

    @ten_nv.setter
    def ten_nv(self, value):
        self._ten_nv = value

    @property
    def luong_co_ban(self):
        return self._luong_co_ban

    @luong_co_ban.setter
    def luong_co_ban(self, value):
        self._luong_co_ban = value

    @property
    def he_so_luong(self):
        return self._he_so_luong

    @he_so_luong.setter
    def he_so_luong(self, value):
        self._he_so_luong = value

    # --- Các phương thức nghiệp vụ ---
    def tinhLuong(self):
        # Lương = luongCoBan × heSoLuong
        return self._luong_co_ban * self._he_so_luong

    def inTTin(self):
        # Hiển thị đầy đủ thông tin
        print(f"Mã NV: {self._ma_nv} | Tên: {self._ten_nv} | Hệ số: {self._he_so_luong} | Tổng lương: {self.tinhLuong():,.0f} đ")

    def tangLuong(self, delta):
        # Kiểm tra LUONG_MAX trước khi quyết định tăng hệ số
        luong_du_kien = self._luong_co_ban * (self._he_so_luong + delta)
        
        if luong_du_kien <= self.LUONG_MAX:
            self._he_so_luong += delta
            print(f"-> Đã tăng hệ số thêm {delta}. Hệ số mới là: {self._he_so_luong}")
        else:
            print(f"-> KHÔNG THỂ TĂNG: Lương dự kiến ({luong_du_kien:,.0f} đ) đã vượt giới hạn {self.LUONG_MAX:,.0f} đ!")

print("--- CHẠY THỬ BT NC ---")
nv_nc = NhanVienNC("NV01", "Nguyễn Văn A", 10000000, 2.5)
nv_nc.inTTin()
nv_nc.tangLuong(1.0) # Tăng hợp lệ
nv_nc.tangLuong(2.0) # Vượt LUONG_MAX