
class Kendaraan:
    def __init__(self):
        print("Class Kendaraan")

    def info(self):
        print("Ini adalah kendaraan")



class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Class Mobil")

    def jalan(self):
        print("Mobil berjalan di jalan raya")



class Motor(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Class Motor")

    def jalan(self):
        print("Motor berjalan di jalan kecil")



class KendaraanDarat(Mobil, Motor):
    def __init__(self):
        super().__init__()
        print("Class KendaraanDarat")

    def jalan(self):
        super().jalan()
        print("Kendaraan darat sedang berjalan")



print("=== Diamond Problem Example ===")

kendaraan = KendaraanDarat()

print("\nMethod Resolution Order:")
print(KendaraanDarat.__mro__)

print("\nMenjalankan Method:")
kendaraan.info()
kendaraan.jalan()