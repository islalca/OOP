class NhanVienT4:
    def __init__(self, ma_nv="", ten_nv="", luong_co_ban=0, he_so_luong=1.0):
        # Theo chuẩn UML, thuộc tính private trong Python dùng 2 dấu gạch dưới (__)
        self.__ma_nv = ma_nv
        self.__ten_nv = ten_nv
        self.__luong_co_ban = luong_co_ban
        self.__he_so_luong = he_so_luong

    # --- Getter/Setter truyền thống chuẩn UML ---
    def get_ma_nv(self):
        return self.__ma_nv
        
    def set_ma_nv(self, ma_nv):
        self.__ma_nv = ma_nv

    def get_ten_nv(self):
        return self.__ten_nv
        
    def set_ten_nv(self, ten_nv):
        self.__ten_nv = ten_nv

    def get_luong_co_ban(self):
        return self.__luong_co_ban
        
    def set_luong_co_ban(self, luong_cb):
        self.__luong_co_ban = luong_cb

    def get_he_so_luong(self):
        return self.__he_so_luong
        
    def set_he_so_luong(self, he_so):
        self.__he_so_luong = he_so

    # --- Các phương thức nghiệp vụ ---
    def tinhLuong(self):
        return self.__luong_co_ban * self.__he_so_luong

    def inTTin(self):
        print(f"Nhân viên: {self.__ten_nv} ({self.__ma_nv}) - Lương: {self.tinhLuong():,.0f} VND")

    def tangLuong(self, delta):
        # Đề không nhắc lại LUONG_MAX ở BT1 Tuần 4, ta chỉ cần tăng hệ số
        self.__he_so_luong += delta
        print(f"Đã tăng hệ số lương của {self.__ten_nv} lên {self.__he_so_luong}")

print("\n--- CHẠY THỬ BT 1 TUẦN 4 ---")
nv_t4 = NhanVienT4("NV99", "Trần Thị B", 12000000, 1.5)
nv_t4.inTTin()

# Thử nghiệm tính đóng gói (đổi tên qua setter)
nv_t4.set_ten_nv("Trần Thị Bách")
nv_t4.tangLuong(0.5)
nv_t4.inTTin()