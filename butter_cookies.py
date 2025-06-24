# Butter Cookies
class ButterCookies(HanariBakery, IBaking, IPackaging, ILabeling):
    def _init_(self, nama, kode, bahan, biaya, harga, topping):
        super()._init_(nama, kode, bahan, biaya, harga)
        self.jenis_topping = topping

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis Topping: {self.jenis_topping}")

    def proses_pengadonan(self): print("Mengaduk adonan butter cookies...")
    def proses_pemanggangan(self): print("Memanggang butter cookies...")
    def proses_topping(self): print("Menambahkan topping ke butter cookies...")
    def bake(self): print("Baking butter cookies...")
    def pack(self): print("Mengemas butter cookies...")
    def label(self): print("Label: Butter Cookies")