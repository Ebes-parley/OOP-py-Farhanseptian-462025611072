import sys


# 1. SUPER-CLASS (INHERITANCE BASE)

class PesananPakaian:
    def __init__(self, id_pesanan, nama_pelanggan, jumlah_pcs, tenggat_waktu, harga_dasar_per_pcs):
        self.id_pesanan = id_pesanan
        self.nama_pelanggan = nama_pelanggan
        self.jumlah_pcs = jumlah_pcs
        self.tenggat_waktu = tenggat_waktu
        self.harga_dasar_per_pcs = harga_dasar_per_pcs
        
        # ENCAPSULATION (Atribut privat/protected)
        self.__total_biaya = 0
        self.__jumlah_dp = 0
        self.__status_pembayaran = "Pending (Belum DP)"
        self.__status_produksi = "Antrean"

    # Encapsulation: Getter & Setter dengan Validasi
    def get_total_biaya(self):
        return self.__total_biaya

    def set_total_biaya(self, nilai):
        if nilai >= 0:
            self.__total_biaya = nilai

    def get_status_pembayaran(self):
        return self.__status_pembayaran

    def get_status_produksi(self):
        return self.__status_produksi

    # Encapsulation: Validasi Pembayaran DP minimal 50%
    def set_bayar_dp(self, nominal):
        if nominal < (self.__total_biaya * 0.5):
            print(f" [GAGAL] DP minimal 50% dari total tagihan (Rp {self.__total_biaya * 0.5:,.0f})")
            return False
        else:
            self.__jumlah_dp = nominal
            self.__status_pembayaran = "Diproses (DP Lunas)"
            self.__status_produksi = "Potong Bahan"
            print(f" [BERHASIL] DP diterima sebesar Rp {nominal:,.0f}. Status pesanan sekarang: DIPROSES.")
            return True

    def update_status_produksi(self, status_baru):
        self.__status_produksi = status_baru

    # POLYMORPHISM (Method dasar yang akan di-override)
    def hitung_biaya_produksi(self):
        total = self.jumlah_pcs * self.harga_dasar_per_pcs
        self.set_total_biaya(total)
        return total

    def tampilkan_info(self):
        print(f"\n--- ID PESANAN: {self.id_pesanan} ---")
        print(f"Pelanggan        : {self.nama_pelanggan}")
        print(f"Jumlah           : {self.jumlah_pcs} pcs")
        print(f"Tenggat Waktu    : {self.tenggat_waktu}")
        print(f"Total Biaya      : Rp {self.get_total_biaya():,.0f}")
        print(f"Status Bayar     : {self.get_status_pembayaran()}")
        print(f"Status Produksi  : {self.get_status_produksi()}")


# ==========================================
# 2. SUB-CLASSES (INHERITANCE & POLYMORPHISM)
# ==========================================
class PesananKaos(PesananPakaian):
    def __init__(self, id_pesanan, nama_pelanggan, jumlah_pcs, tenggat_waktu, jenis_sablon):
        super().__init__(id_pesanan, nama_pelanggan, jumlah_pcs, tenggat_waktu, harga_dasar_per_pcs=55000)
        self.jenis_sablon = jenis_sablon

    # Polymorphism: Override kalkulasi biaya sablon
    def hitung_biaya_produksi(self):
        biaya_sablon = 10000 if self.jenis_sablon.lower() == "plastisol" else 5000
        total = self.jumlah_pcs * (self.harga_dasar_per_pcs + biaya_sablon)
        self.set_total_biaya(total)
        return total

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kategori         : Kaos (Sablon: {self.jenis_sablon})")


class PesananKorsa(PesananPakaian):
    def __init__(self, id_pesanan, nama_pelanggan, jumlah_pcs, tenggat_waktu, jenis_kancing, pakai_puring):
        super().__init__(id_pesanan, nama_pelanggan, jumlah_pcs, tenggat_waktu, harga_dasar_per_pcs=90000)
        self.jenis_kancing = jenis_kancing
        self.pakai_puring = pakai_puring

    def hitung_biaya_produksi(self):
        biaya_tambahan = 15000 if self.pakai_puring else 0
        total = self.jumlah_pcs * (self.harga_dasar_per_pcs + biaya_tambahan)
        self.set_total_biaya(total)
        return total

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kategori         : Korsa (Puring: {'Ya' if self.pakai_puring else 'Tidak'})")


class PesananJaket(PesananPakaian):
    def __init__(self, id_pesanan, nama_pelanggan, jumlah_pcs, tenggat_waktu, jenis_resleting, bahan_furing):
        super().__init__(id_pesanan, nama_pelanggan, jumlah_pcs, tenggat_waktu, harga_dasar_per_pcs=130000)
        self.jenis_resleting = jenis_resleting
        self.bahan_furing = bahan_furing

    # Polymorphism: Override kalkulasi biaya jaket (Resleting Premium / Furing)
    def hitung_biaya_produksi(self):
        biaya_resleting = 15000 if self.jenis_resleting.lower() == "ykk" else 5000
        biaya_furing = 10000 if self.bahan_furing.lower() == "despo" else 5000
        total = self.jumlah_pcs * (self.harga_dasar_per_pcs + biaya_resleting + biaya_furing)
        self.set_total_biaya(total)
        return total

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kategori         : Jaket (Resleting: {self.jenis_resleting}, Furing: {self.bahan_furing})")


# ==========================================
# 3. CONTROLLER & INTERFACE CLI
# ==========================================
class ConfectionerySystemCLI:
    def __init__(self):
        self.daftar_pesanan = []
        self.counter_id = 1

    def menu_utama(self):
        while True:
            print("\n" + "="*45)
            print("  CONFECTIONERY PRODUCTION SYSTEM (CLI)")
            print("="*45)
            print("1. Tambah Pesanan Baru")
            print("2. Bayar DP (Validasi Encapsulation)")
            print("3. Update Status Produksi")
            print("4. Lihat Semua Pesanan")
            print("5. Keluar")
            pilihan = input("Pilih menu (1-5): ")

            if pilihan == "1":
                self.tambah_pesanan()
            elif pilihan == "2":
                self.bayar_dp()
            elif pilihan == "3":
                self.update_status()
            elif pilihan == "4":
                self.lihat_pesanan()
            elif pilihan == "5":
                print("Terima kasih! Keluar dari sistem...")
                sys.exit()
            else:
                print("Pilihan tidak valid!")

    def tambah_pesanan(self):
        print("\n--- TAMBAH PESANAN ---")
        nama = input("Nama Pelanggan: ")
        jumlah = int(input("Jumlah (pcs): "))
        tenggat = input("Tenggat Waktu (YYYY-MM-DD): ")
        
        print("\nJenis Pakaian:")
        print("1. Kaos")
        print("2. Korsa")
        print("3. Jaket")
        jenis = input("Pilih (1-3): ")

        id_str = f"PO-{self.counter_id:03d}"
        pesanan = None

        if jenis == "1":
            sablon = input("Jenis Sablon (Plastisol/Rubber): ")
            pesanan = PesananKaos(id_str, nama, jumlah, tenggat, sablon)
        elif jenis == "2":
            kancing = input("Jenis Kancing: ")
            puring = input("Pakai Puring? (y/n): ").lower() == 'y'
            pesanan = PesananKorsa(id_str, nama, jumlah, tenggat, kancing, puring)
        elif jenis == "3":
            resleting = input("Jenis Resleting (YKK/Biasa): ")
            furing = input("Bahan Furing (Despo/Jaring): ")
            pesanan = PesananJaket(id_str, nama, jumlah, tenggat, resleting, furing)

        if pesanan:
            # Panggil polimorfisme untuk hitung biaya
            total = pesanan.hitung_biaya_produksi()
            self.daftar_pesanan.append(pesanan)
            self.counter_id += 1
            print(f"\nBerhasil Pesanan berhasil dibuat dengan Total Biaya: Rp {total:,.0f}")

    def bayar_dp(self):
        print("\n--- PEMBAYARAN DP ---")
        id_search = input("Masukkan ID Pesanan (misal PO-001): ")
        pesanan = self._cari_pesanan(id_search)
        
        if pesanan:
            print(f"Total Biaya Pesanan: Rp {pesanan.get_total_biaya():,.0f}")
            nominal = float(input("Masukkan Nominal DP: Rp "))
            # Memanggil fungsi Encapsulation
            pesanan.set_bayar_dp(nominal)
        else:
            print("Gagal ID Pesanan tidak ditemukan!")

    def update_status(self):
        print("\n--- UPDATE STATUS PRODUKSI ---")
        id_search = input("Masukkan ID Pesanan: ")
        pesanan = self._cari_pesanan(id_search)

        if pesanan:
            print("Pilih Status Baru:")
            print("1. Potong Bahan")
            print("2. Sablon / Bordir")
            print("3. Penjahitan")
            print("4. Finishing & QC")
            print("5. Selesai")
            st = input("Pilih (1-5): ")
            list_st = ["Potong Bahan", "Sablon / Bordir", "Penjahitan", "Finishing & QC", "Selesai"]
            if 1 <= int(st) <= 5:
                pesanan.update_status_produksi(list_st[int(st)-1])
                print("oke Status produksi berhasil diperbarui!")
        else:
            print("Gagal ID Pesanan tidak ditemukan!")

    def lihat_pesanan(self):
        if not self.daftar_pesanan:
            print("\nBelum ada pesanan tersimpan.")
            return
        for p in self.daftar_pesanan:
            p.tampilkan_info()

    def _cari_pesanan(self, id_pesanan):
        for p in self.daftar_pesanan:
            if p.id_pesanan.lower() == id_pesanan.lower():
                return p
        return None

if __name__ == "__main__":
    app = ConfectionerySystemCLI()
    app.menu_utama()