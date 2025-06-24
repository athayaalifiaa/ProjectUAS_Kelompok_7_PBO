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
    def __init__(self, nama_produk, kode_produk, bahan_baku, biaya_produksi, harga_jual, jenis_topping, waktu_pengembangan):
        self.nama_produk = nama_produk
        self.kode_produk = kode_produk
        self.bahan_baku = bahan_baku  # dictionary
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual
        self.jenis_topping = jenis_topping
        self.waktu_pengembangan = waktu_pengembangan

    def tampilkan_info(self):
        print(f"\n=== {self.nama_produk.upper()} ({self.kode_produk}) ===")
        print("Bahan Baku:")
        for b, j in self.bahan_baku.items():
            print(f"- {b}: {j}")
        print(f"Biaya Produksi: Rp{self.biaya_produksi}")
        print(f"Harga Jual: Rp{self.harga_jual}")
        print(f"Topping: {self.jenis_topping}")
        print(f"Waktu Pengembangan: {self.waktu_pengembangan} menit")

    def estimasi_profit(self, jumlah_pcs):
        return (self.harga_jual - self.biaya_produksi) * jumlah_pcs

    @abstractmethod
    def proses_pengadonan(self): pass

    @abstractmethod
    def proses_pemanggangan(self): pass

    @abstractmethod
    def proses_topping(self): pass

    def proses_pengembangan(self):
        print("Tidak memerlukan proses pengembangan.")

# Subclass
class RotiManis(HanariBakery, IBaking, IPackaging, ILabeling):
    def proses_pengadonan(self): print("Mengaduk adonan roti manis...")
    def proses_pengembangan(self): print("Proofing roti manis...")
    def proses_pemanggangan(self): print("Memanggang roti manis...")
    def bake(self): print("Baking roti manis...")
    def pack(self): print("Mengemas roti manis...")
    def label(self): print("Label: Roti Manis")

class Croissant(HanariBakery, IBaking, IPackaging, ILabeling):
    def proses_pengadonan(self): print("Mengaduk adonan croissant...")
    def proses_pengembangan(self): print("Melipat dan proofing croissant...")
    def proses_pemanggangan(self): print("Memanggang croissant...")
    def bake(self): print("Baking croissant...")
    def pack(self): print("Mengemas croissant...")
    def label(self): print("Label: Croissant")

class ButterCookies(HanariBakery, IBaking, IPackaging, ILabeling):
    def proses_pengadonan(self): print("Mengaduk adonan butter cookies...")
    def proses_pemanggangan(self): print("Memanggang butter cookies...")
    def proses_topping(self): print("Menambahkan gula tabur...")
    def bake(self): print("Baking butter cookies...")
    def pack(self): print("Mengemas butter cookies...")
    def label(self): print("Label: Butter Cookies")

class Muffin(HanariBakery, IBaking, IPackaging, ILabeling):
    def proses_pengadonan(self): print("Mengaduk adonan muffin...")
    def proses_pengembangan(self): print("Proofing muffin...")
    def proses_pemanggangan(self): print("Memanggang muffin...")
    def proses_topping(self): print("Menambahkan topping buah...")
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
    topping = input("Jenis topping: ")
    waktu = input("Waktu pengembangan (menit): ")
    bahan = {}
    while True:
        bhn = input("Nama bahan (done = selesai): ")
        if bhn == "done": break
        jumlah = input(f"Jumlah {bhn}: ")
        bahan[bhn] = jumlah
    biaya = int(input("Biaya produksi: "))
    harga = int(input("Harga jual: "))

    cls = {"roti manis": RotiManis, "croissant": Croissant, "butter cookies": ButterCookies, "muffin": Muffin}
    if jenis in cls:
        produk = cls[jenis](nama, kode, bahan, biaya, harga, topping, waktu)
        produk_list.append(produk)
        print("Produk berhasil ditambahkan!")
    else:
        print("Jenis tidak dikenali.")

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
            p.proses_pengembangan()
            p.proses_pemanggangan()
            p.proses_topping()
            p.bake()
            p.pack()
            p.label()
            return
    print("Produk tidak ditemukan.")

if __name__ == "__main__":
    menu()