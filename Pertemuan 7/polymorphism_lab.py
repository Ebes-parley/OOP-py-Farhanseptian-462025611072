class Guru: 
    def __init__(self, nama: str):
        self.nama = nama

    def mengajar(self):
        print(f"{self.nama} sedang mengajar di kelas.")

class Guru_IPA(Guru):
    def mengajar(self):
        print(f"Guru IPA {self.nama} sedang mengajar rumus-rumus matematika.")

class Guru_sejarah(Guru):
    def mengajar(self):
        print(f"Guru sejarah {self.nama} sedang mengajar tata bahasa dan sastra.")           

def simulasikan_mengajar(guru):  
    guru.mengajar()

guru_umum = Guru("Pak Joko") 
guru_mtk = Guru_IPA("Bu Indah")
guru_bhs = Guru_sejarah("Pak mul")

print("--- Simulasi Mengajar (Dengan Polymorphism) ---")
simulasikan_mengajar(guru_umum)  
simulasikan_mengajar(guru_mtk)    
simulasikan_mengajar(guru_bhs)