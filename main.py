

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

if __name__ == "_main_":
    menu()