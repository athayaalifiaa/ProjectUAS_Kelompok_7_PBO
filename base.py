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