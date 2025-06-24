class Muffin(HanariBakery, IBaking, IPackaging, ILabeling):
    def _init_(self, nama, kode, bahan, biaya, harga, topping, waktu):
        super()._init_(nama, kode, bahan, biaya, harga)
        self.jenis_topping = topping
        self.waktu_pengembangan = waktu

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis Topping: {self.jenis_topping}")
        print(f"Waktu Pengembangan: {self.waktu_pengembangan} menit")

    def proses_pengadonan(self): print("Mengaduk adonan muffin...")
    def proses_pengembangan(self): print("Proofing muffin...")
    def proses_pemanggangan(self): print("Memanggang muffin...")
    def proses_topping(self): print("Menambahkan topping ke muffin...")
    def bake(self): print("Baking muffin...")
    def pack(self): print("Mengemas muffin...")
    def label(self): print("Label: Muffin")