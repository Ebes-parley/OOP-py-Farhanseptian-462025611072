class Kalkulator:
    angka1 = 0
    angka2 = 0

    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def panggil_angka1(self):
        return f"angka1 = {self.angka1}"
    def panggil_angka2(self):
        return f"angka2 = {self.angka2}"

    @staticmethod
    def pertambahan_3angka(a, b, c):
        return f"{a + b + c}"

kalkulator1 = Kalkulator(9, 10)
print(kalkulator1.panggil_angka1(), kalkulator1.panggil_angka2())
print(Kalkulator.pertambahan_3angka(1,2,3))