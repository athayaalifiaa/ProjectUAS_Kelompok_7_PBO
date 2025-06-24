# Roti Manis
class RotiManis(HanariBakery, IBaking, IPackaging, ILabeling):
    def __init__(self, nama, kode, bahan, biaya, harga, waktu):
        super().__init__(nama, kode, bahan, biaya, harga)
        self.waktu_pengembangan = waktu

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Waktu Pengembangan: {self.waktu_pengembangan} menit")

    def proses_pengadonan(self): print("Mengaduk adonan roti manis...")
    def proses_pengembangan(self): print("Proofing roti manis...")
    def proses_pemanggangan(self): print("Memanggang roti manis...")
    def bake(self): print("Baking roti manis...")
    def pack(self): print("Mengemas roti manis...")
    def label(self): print("Label: Roti Manis")
