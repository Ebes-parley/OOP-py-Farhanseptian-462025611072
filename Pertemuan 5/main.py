class Medsos:
    __email = '' 
    __name = ''
    __pewe = ''

    def __init__(self, email, name, pewe):
        self.__email = email
        self.__name = name
        self.__pewe = pewe
    
    def get_email(self):
        return self.__email
    def get_name(self):
        return self.__name
    def get_pewe(self):
        return self.__pewe
    
    def Login(self, pewe_input):
        if pewe_input != self.__pewe:
            print('jika pewe salah anda diblok')
            return
        self.__pewe = 'sohih'
        print (f' selamat anda berhasil login atas nama {self.__name} berhasil login')

account1 = Medsos('parle@gmail.com','parle', '1236')
#pembuktian tidak dapat mengakses private langsung 
# program akan menghasilkan error: AttributeError: 'Absensi' object has no attribute '__pin'

account1.Login('0000')#contoh misal nih kalo salah yaa
account1.Login('1236')#nah ini kalo benar

print(f'email:{account1.get_email()}')
print(f'nama:{account1.get_name()}')

account2 = Medsos('bangle@gmail.com', 'bangle', '159')
account2.Login('0000')#contoh misal nih kalo salah yaa
account2.Login('159')#nah ini kalo benar

print(f'email:{account2.get_email()}')
print(f'nama:{account2.get_name()}')
      