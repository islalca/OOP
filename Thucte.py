class ConCho:
    def __init__(self, ten, giong, tuoi, mau_long, can_nang):
        self.ten = ten
        self.giong = giong
        self.tuoi = tuoi
        self.mau_long = mau_long
        self.can_nang = can_nang
    
    def in_thong_tin(self):
        print(f"Bé cún tên là {self.ten}, giống {self.giong}, {self.tuoi} tuổi, lông màu {self.mau_long}, nặng {self.can_nang}kg.")

    def sua(self):
        print(f"{self.ten}: Gâu gâu! 🐕")

    def an(self, thuc_an):
        print(f"{self.ten} đang ăn {thuc_an}. Măm măm...")

        self.can_nang += 0.2
        print(f"-> Cân nặng hiện tại: {self.can_nang:.1f}kg")

    def ngu(self):
        print(f"{self.ten} đang cuộn tròn ngủ: khò... khò... 💤")


print("--- KHỞI TẠO ĐỐI TƯỢNG ---")
cho_1 = ConCho(ten="Milu", giong="Corgi", tuoi=2, mau_long="Vàng trắng", can_nang=12.0)
cho_2 = ConCho(ten="Ngáo", giong="Husky", tuoi=3, mau_long="Xám đen", can_nang=25.0)

print("\n--- GỌI PHƯƠNG THỨC CỦA ĐỐI TƯỢNG ---")
cho_1.in_thong_tin()
cho_1.sua()
cho_1.an("xúc xích")

print("-" * 20)

cho_2.in_thong_tin()
cho_2.ngu()