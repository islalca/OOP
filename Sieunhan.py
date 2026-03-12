# Định nghĩa lớp SieuNhan
class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def hien_thi_thong_tin(self):
        print(f"Tên: {self.ten} | Vũ khí: {self.vu_khi} | Màu: {self.mau_sac}")

print("--- KẾT QUẢ BÀI 2 ---")
# Khởi tạo 2 đối tượng siêu nhân
sieu_nhan_1 = SieuNhan("Gao Đỏ", "Kiếm Gao", "Đỏ")
sieu_nhan_2 = SieuNhan("Batman", "Phi tiêu Batarang", "Đen")

# Hiển thị thông tin để kiểm tra
sieu_nhan_1.hien_thi_thong_tin()
sieu_nhan_2.hien_thi_thong_tin()