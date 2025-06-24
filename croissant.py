# Croissant
class Croissant(HanariBakery, IBaking, IPackaging, ILabeling):
    def __init__(self, nama, kode, bahan, biaya, harga, waktu):
        super().__init__(nama, kode, bahan, biaya, harga)
        self.waktu_pengembangan = waktu

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Waktu Pengembangan: {self.waktu_pengembangan} menit")

    def proses_pengadonan(self): print("Mengaduk adonan croissant...")
    def proses_pengembangan(self): print("Melipat dan proofing croissant...")
    def proses_pemanggangan(self): print("Memanggang croissant...")
    def bake(self): print("Baking croissant...")
    def pack(self): print("Mengemas croissant...")
    def label(self): print("Label: Croissant")