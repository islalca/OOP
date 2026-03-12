# Định nghĩa lại lớp SieuNhan cho bài 3
class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def hien_thi_thong_tin(self):
        print(f"- {self.ten} (Vũ khí: {self.vu_khi}, Màu: {self.mau_sac})")

# Tạo một danh sách (list) rỗng để chứa các đối tượng siêu nhân
danh_sach_sieu_nhan = []

print("--- NHẬP DANH SÁCH SIÊU NHÂN ---")
# 1. Dùng vòng lặp while để nhập liên tục
while True:
    ten_nhap = input("Nhập tên siêu nhân: ")
    vu_khi_nhap = input("Nhập vũ khí: ")
    mau_sac_nhap = input("Nhập màu sắc: ")
    
    # Tạo đối tượng từ dữ liệu nhập và thêm vào danh sách
    sn_moi = SieuNhan(ten_nhap, vu_khi_nhap, mau_sac_nhap)
    danh_sach_sieu_nhan.append(sn_moi)
    
    # Hỏi người dùng có muốn nhập tiếp không
    cau_tra_loi = input("Bạn có muốn nhập thêm không? (y/n): ")
    if cau_tra_loi.lower() != 'y':
        break # Thoát vòng lặp while nếu không nhập 'y'

print("\n--- HIỂN THỊ DANH SÁCH ---")
# 2. Dùng vòng lặp for để duyệt qua danh sách và in thông tin
for sn in danh_sach_sieu_nhan:
    sn.hien_thi_thong_tin()