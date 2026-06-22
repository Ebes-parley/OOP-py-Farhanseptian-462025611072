class NilaiMinimalError(Exception):
    def __init__(self, message="Nilai mahasiswa tidak boleh kurang dari 0 dan tidak boleh lebih dari 100"):
        self.message = message
        super().__init__(self.message)
class NilaiMahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.nilai = None

    def input_nilai(self):
        try:
            nilai_input = float(input(f"masukkan nilai{self.nama}(0-100)"))
            if nilai_input < 0 or nilai_input > 100:
                raise NilaiMinimalError()
            self.nilai = nilai_input
            print(f"Nilai{self.nama}adalah{self.nilai}")
        except NilaiMinimalError as e:
            print(f"error: {e}")
        except ValueError:
            print("Error: Input harus berupa angka.")
        finally:
            print("Proses pemeriksaan nilai selesai.\n")

if __name__ == "__main__":
    mahasiswa1 = NilaiMahasiswa("Andi")
    mahasiswa1.input_nilai()
    mahasiswa2 = NilaiMahasiswa("Parley")
    mahasiswa2.input_nilai()