class Gamer :
    user = ''
    skor = 0
    level = 0

    def cek_nama(self):
        print(f"hey {self.user} kamu memperoleh Scor {self.skor} dengan Level{self.level}")

    def __init__(self, user='', skor=0, level=0):
        if skor < 0:
            raise ValueError("skor gk boleh negative")
        self.user = user
        self.skor = skor
        self.level = level
        print ("nama anda sudah terdaftar")

    def __str__(self):
        return f"user= {self.user} - skor= {self.skor} - level={self.level}"
    def __eq__(self, other):
        return self.user == other.user and self.skor == other. skor and self.level == other. level
    def __ge__(self, other):
        return self.skor >= other.skor
    def __le__(self, other):
        return self.skor <= other.skor
    
user1= Gamer("bangler", 9000, 9)
user1.cek_nama()
user2 = Gamer ("Oheb", 8561, 7)
user2.cek_nama()
user3= Gamer("Farhan", 9999, 100)
user3.cek_nama()

print(user1)
print(user2 <= user3)
print(user3 >= user1)