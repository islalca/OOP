class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def hien_thi(self):
        return f"Tên: {self.ho_ten} | Tuổi: {self.tuoi} | Giới tính: {self.gioi_tinh} | Địa chỉ: {self.dia_chi}"

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac # 1 đến 10

    def hien_thi(self):
        return f"[Công Nhân] {super().hien_thi()} | Bậc: {self.bac}/10"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def hien_thi(self):
        return f"[Kỹ Sư] {super().hien_thi()} | Ngành: {self.nganh_dao_tao}"

class NhanVienThuocCanBo(CanBo): # Đổi tên xíu để không trùng với bài 2 nếu chạy chung file
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi(self):
        return f"[Nhân Viên] {super().hien_thi()} | Công việc: {self.cong_viec}"

class QLCB:
    def __init__(self):
        self.danh_sach_can_bo = []

    def them_can_bo(self, can_bo):
        self.danh_sach_can_bo.append(can_bo)
        print(f"Đã thêm: {can_bo.ho_ten}")

    def tim_kiem_theo_ten(self, ten_tim_kiem):
        ket_qua = [cb for cb in self.danh_sach_can_bo if ten_tim_kiem.lower() in cb.ho_ten.lower()]
        if not ket_qua:
            print("Không tìm thấy cán bộ nào!")
        else:
            print(f"--- KẾT QUẢ TÌM KIẾM '{ten_tim_kiem}' ---")
            for cb in ket_qua:
                print(cb.hien_thi())

    def hien_thi_danh_sach(self):
        print("--- DANH SÁCH CÁN BỘ ---")
        for cb in self.danh_sach_can_bo:
            print(cb.hien_thi())

print("\n--- BT3: QUẢN LÝ CÁN BỘ ---")
quan_ly = QLCB()

# 1. Thêm mới
quan_ly.them_can_bo(CongNhan("Lê Văn Bảy", 30, "Nam", "Hải Phòng", 5))
quan_ly.them_can_bo(KySu("Trần Thị Chín", 28, "Nữ", "Hà Nội", "Công nghệ Thông tin"))
quan_ly.them_can_bo(NhanVienThuocCanBo("Phạm Văn Mười", 25, "Nam", "Đà Nẵng", "Lễ tân"))

# 2. Hiển thị danh sách
quan_ly.hien_thi_danh_sach()

# 3. Tìm kiếm
quan_ly.tim_kiem_theo_ten("Chín")