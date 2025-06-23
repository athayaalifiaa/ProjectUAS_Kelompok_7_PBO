
from abc import ABC, abstractmethod


class Baking(ABC):
    @abstractmethod
    def bake(self): pass

class Packaging(ABC):
    @abstractmethod
    def pack(self): pass

class Labeling(ABC):
    @abstractmethod
    def label(self): pass

# Abstract Class
class ProdukRoti(ABC):
    def __init__(self, nama, kode, bahan, biaya, harga):
        self.nama = nama
        self.kode = kode
        self.bahan = bahan  
        self.biaya = biaya
        self.harga = harga

    def tampil_info(self):
        print(f"\n=== {self.nama.upper()} ({self.kode}) ===")
        print("Bahan Baku:")
        for b, j in self.bahan.items():
            print(f"- {b}: {j}")
        print(f"Biaya Produksi: Rp{self.biaya}")
        print(f"Harga Jual: Rp{self.harga}")

    def hitung_profit(self, jumlah):
        return (self.harga - self.biaya) * jumlah

    @abstractmethod
    def pengadonan(self): pass

    def pengembangan(self):
        print("Tidak perlu proses pengembangan.")

    @abstractmethod
    def pemanggangan(self): pass

    @abstractmethod
    def topping(self): pass

# Subclasses
class RotiManis(ProdukRoti, Baking, Packaging, Labeling):
    def pengadonan(self): print("Mengaduk adonan roti manis...")
    def pengembangan(self): print("Proofing adonan roti manis...")
    def pemanggangan(self): print("Memanggang roti manis...")
    def topping(self): print("Menambahkan topping manis...")
    def bake(self): print("Baking roti manis...")
    def pack(self): print("Mengemas roti manis...")
    def label(self): print("Memberi label Roti Manis.")

class Croissant(ProdukRoti, Baking, Packaging, Labeling):
    def pengadonan(self): print("Mengaduk adonan croissant...")
    def pengembangan(self): print("Melipat dan fermentasi croissant...")
    def pemanggangan(self): print("Memanggang croissant...")
    def topping(self): print("Menambahkan butter glaze...")
    def bake(self): print("Baking croissant...")
    def pack(self): print("Mengemas croissant...")
    def label(self): print("Memberi label Croissant.")

class ButterCookies(ProdukRoti, Baking, Packaging, Labeling):
    def pengadonan(self): print("Mengaduk adonan butter cookies...")
    def pemanggangan(self): print("Memanggang butter cookies...")
    def topping(self): print("Menambahkan taburan gula...")
    def bake(self): print("Baking butter cookies...")
    def pack(self): print("Mengemas butter cookies...")
    def label(self): print("Memberi label Butter Cookies.")

class Muffin(ProdukRoti, Baking, Packaging, Labeling):
    def pengadonan(self): print("Mengaduk adonan muffin...")
    def pengembangan(self): print("Proofing adonan muffin...")
    def pemanggangan(self): print("Memanggang muffin...")
    def topping(self): print("Menambahkan topping buah...")
    def bake(self): print("Baking muffin...")
    def pack(self): print("Mengemas muffin...")
    def label(self): print("Memberi label Muffin.")

# Penyimpanan produk
produk_list = []

# Menu CLI

def menu():
    while True:
        print("\n====== HANARI BAKERY SYSTEM ======")
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Kalkulator Estimasi Profit")
        print("4. Simulasi Produksi")
        print("0. Keluar")

        pilih = input("Pilih menu: ")
        if pilih == "1": tambah_produk()
        elif pilih == "2": tampilkan_produk()
        elif pilih == "3": kalkulator_profit()
        elif pilih == "4": simulasi_produksi()
        elif pilih == "0": print("Terima kasih!"); break
        else: print("Pilihan tidak valid.")

def tambah_produk():
    print("\n-- Tambah Produk --")
    nama = input("Nama produk: ")
    kode = input("Kode produk: ")
    jenis = input("Jenis produk (roti manis / croissant / butter cookies / muffin): ").lower()
    bahan = {}
    while True:
        bhn = input("Nama bahan (ketik 'done' jika selesai): ")
        if bhn == "done": break
        jumlah = input(f"Jumlah {bhn}: ")
        bahan[bhn] = jumlah
    biaya = int(input("Biaya produksi per-n pcs: "))
    harga = int(input("Harga jual per-n pcs: "))

    produk = None
    if jenis == "roti manis":
        produk = RotiManis(nama, kode, bahan, biaya, harga)
    elif jenis == "croissant":
        produk = Croissant(nama, kode, bahan, biaya, harga)
    elif jenis == "butter cookies":
        produk = ButterCookies(nama, kode, bahan, biaya, harga)
    elif jenis == "muffin":
        produk = Muffin(nama, kode, bahan, biaya, harga)
    else:
        print("Jenis tidak dikenali.")
        return

    produk_list.append(produk)
    print("Produk berhasil ditambahkan!")

def tampilkan_produk():
    if not produk_list:
        print("Belum ada produk.")
    for p in produk_list:
        p.tampil_info()

def kalkulator_profit():
    tampilkan_produk()
    kode = input("\nMasukkan kode produk untuk estimasi: ")
    jumlah = int(input("Jumlah pcs yang akan diproduksi: "))
    for p in produk_list:
        if p.kode == kode:
            profit = p.hitung_profit(jumlah)
            print(f"Estimasi profit: Rp{profit}")
            return
    print("Produk tidak ditemukan.")

def simulasi_produksi():
    tampilkan_produk()
    kode = input("\nMasukkan kode produk untuk simulasi: ")
    for p in produk_list:
        if p.kode == kode:
            print("\n-- Simulasi Produksi --")
            p.pengadonan()
            p.pengembangan()
            p.pemanggangan()
            p.topping()
            p.bake()
            p.pack()
            p.label()
            return
    print("Produk tidak ditemukan.")

if __name__ == "__main__":
    menu()