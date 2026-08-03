class konveksi:
    def __init__(self):
        print("selamat datang di konveksi kami")
    def info(self):
        print("disini kami menyediakan beberapa jenis pakaian")

class jersey:
    def __init__(self):
        print("jersey di sini adalah kelas top")

class katun:
    def __init__(self):
        print("katun di sini adalah kelas tertinggi katun")

class atas(jersey):
    def __init__(self):
        super().__init__()
        print("jersey")

class sablon(katun):
    def __init__(self):
        super().__init__()
        print("ada dua jenis sablon katun dtf dan plastisol")

class jaket:
    def __init__(self):
        super().__init__()
        print("jaket di sini adalah pakaian luaran yang sangat kece")

class luaran(jaket):
    def __init__(self):
        super().__init__()
        print("Biar Lu makin kece")

konveksi()
jersey()
katun()
jaket()

class pemesananpakaian:
    def __init__(self, id_pemesanan, nama_pelanggan, jumlah_pcs, tanggal_waktu, harga_dasar_per_pcs):
        self.id_pemesanan = id_pemesanan
        self.nama_pelanggan = nama_pelanggan
        self.jumlah_pcs = jumlah_pcs
        self.tanggal_waktu = tanggal_waktu
        self.harga_dasar_per_pcs = harga_dasar_per_pcs

        self.__total_biaya = 0
        self.__jumlah_dp = 0
        self.__status_pembayaran = "pending (Belum Dp)"
        self.__status_produksi = "antrean"

def get_total_biaya(self):
    return self.__total_biaya
def set_total_biaya(self, nilai):
    if nilai >= 0:
        self.__total_biaya = nilai
def get_status_pembayaran(self):
    return self.__status_pembayaran
def get_status_produksi(self):
    return self.__status_produksi

def set_bayar_dp (self, nominal):
    if nominal < (self.__total.__biaya * 0.5):
        print("[gagal] Dp minimal 50% dari total tagihan (Rp {self.__totalb_biaya * 0.5:,.0f})")
        return False
    else: 
        self.jumlah_dp = nominal
        self.__status_pembayaran = "diproses (DPlunas)"
        self.__status_produkso = "potong bahan" 
        print("Berhasil diterima sebesar Rp{nominal:,.0f}. status pembayaran sekarang: Diproses" )
        return True
def update_status_pembayaran(self, status_baru):
    self.__status_produksi = status_baru



