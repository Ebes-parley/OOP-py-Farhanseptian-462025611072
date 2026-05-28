class lele:
    jenis =""
    Air =""
    warna  =""

    def __init__(self, jenis,Air,warna):
        self.jenis = jenis
        self.Air = Air
        self.warna = warna

    def panggil_jenis(self):
        return f"ini ikan lele {self.jenis}"
    def panggil_Air(self):
        return f"dari Air {self.Air}"
    def panggil_warna(self):
        return f"warnanya {self.warna}"
    

lele1=lele("Albino","Tawar","Putih")
print(lele1.panggil_jenis(), lele1.panggil_Air(), lele1.panggil_warna())
lele2=lele("Hias","Asin","Hitam legam")
print(lele2.panggil_jenis(), lele2.panggil_Air(), lele2.panggil_warna())
