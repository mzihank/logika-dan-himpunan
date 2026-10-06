USERNAME_TERDAFTAR = "zihankholidi"
PASSWORD_TERDAFTAR = "zihan123"
akun_aktif = True

username = input("Username: ")
password = input("Password: ")

username_benar = username == USERNAME_TERDAFTAR
password_benar = password == PASSWORD_TERDAFTAR

login = username_benar and password_benar and akun_aktif

if login:
    print("Login berhasil")
elif not username_benar:
    print("Username salah")
elif not password_benar:
    print("Password salah")
else:
    print("Akun tidak aktif")
