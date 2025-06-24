from abc import ABC, abstractmethod

# Interfaces
class IBaking(ABC):
    @abstractmethod
    def bake(self): pass

class IPackaging(ABC):
    @abstractmethod
    def pack(self): pass

class ILabeling(ABC):
    @abstractmethod
    def label(self): pass

# Abstract Class
class HanariBakery(ABC):
    def __init__(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual):
        self.nama_produk = nama_produk
        self.kode_produk = kode_produk
        self.bahan_baku = bahan_baku  # dictionary
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    def tampilkan_info(self):
        print(f"\n=== {self.nama_produk.upper()} ({self.kode_produk}) ===")
        print("Bahan Baku:")
        for b, j in self.bahan_baku.items():
            print(f"- {b}: {j}")
        print(f"Biaya Produksi: Rp{self.biaya_produksi}")
        print(f"Harga Jual: Rp{self.harga_jual}")

    def estimasi_profit(self, jumlah_pcs):
        return (self.harga_jual - self.biaya_produksi) * jumlah_pcs

    @abstractmethod
    def proses_pengadonan(self): pass

    @abstractmethod
    def proses_pemanggangan(self): pass

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

# Butter Cookies
class ButterCookies(HanariBakery, IBaking, IPackaging, ILabeling):
    def __init__(self, nama, kode, bahan, biaya, harga, topping):
        super().__init__(nama, kode, bahan, biaya, harga)
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

# Muffin
class Muffin(HanariBakery, IBaking, IPackaging, ILabeling):
    def __init__(self, nama, kode, bahan, biaya, harga, topping, waktu):
        super().__init__(nama, kode, bahan, biaya, harga)
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

# CLI & Data
produk_list = []

def menu():
    while True:
        print("\n===== HANARI BAKERY SYSTEM =====")
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Estimasi Profit")
        print("4. Simulasi Produksi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1": tambah_produk()
        elif pilihan == "2": tampilkan_produk()
        elif pilihan == "3": kalkulator_profit()
        elif pilihan == "4": simulasi_produksi()
        elif pilihan == "0": break
        else: print("Pilihan tidak valid.")

def tambah_produk():
    print("\n-- Tambah Produk --")
    nama = input("Nama produk: ")
    kode = input("Kode produk: ")
    jenis = input("Jenis (roti manis/croissant/butter cookies/muffin): ").lower()
    bahan = {}
    while True:
        bhn = input("Nama bahan (done = selesai): ")
        if bhn == "done": break
        jumlah = input(f"Jumlah {bhn}: ")
        bahan[bhn] = jumlah
    biaya = int(input("Biaya produksi: "))
    harga = int(input("Harga jual: "))

    if jenis == "roti manis":
        waktu = int(input("Waktu pengembangan (menit): "))
        produk = RotiManis(nama, kode, bahan, biaya, harga, waktu)
    elif jenis == "croissant":
        waktu = int(input("Waktu pengembangan (menit): "))
        produk = Croissant(nama, kode, bahan, biaya, harga, waktu)
    elif jenis == "butter cookies":
        topping = input("Jenis topping: ")
        produk = ButterCookies(nama, kode, bahan, biaya, harga, topping)
    elif jenis == "muffin":
        topping = input("Jenis topping: ")
        waktu = int(input("Waktu pengembangan (menit): "))
        produk = Muffin(nama, kode, bahan, biaya, harga, topping, waktu)
    else:
        print("Jenis tidak dikenali.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan!")

def tampilkan_produk():
    if not produk_list:
        print("Belum ada produk.")
    for p in produk_list:
        p.tampilkan_info()

def kalkulator_profit():
    kode = input("Masukkan kode produk: ")
    jumlah = int(input("Jumlah pcs: "))
    for p in produk_list:
        if p.kode_produk == kode:
            profit = p.estimasi_profit(jumlah)
            print(f"Estimasi profit: Rp{profit}")
            return
    print("Produk tidak ditemukan.")

def simulasi_produksi():
    kode = input("Masukkan kode produk: ")
    for p in produk_list:
        if p.kode_produk == kode:
            print("\n-- Simulasi Produksi --")
            p.proses_pengadonan()
            if hasattr(p, 'proses_pengembangan'):
                try:
                    p.proses_pengembangan()
                except: pass
            p.proses_pemanggangan()
            if hasattr(p, 'proses_topping'):
                try:
                    p.proses_topping()
                except: pass
            p.bake()
            p.pack()
            p.label()
            return
    print("Produk tidak ditemukan.")

if __name__ == "__main__":
    menu()