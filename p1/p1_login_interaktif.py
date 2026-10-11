USERNAME_TERDAFTAR = "zihankholidi"
PASSWORD_TERDAFTAR = "zihan123"
akun_aktif = True

username = input("Username: ")
password = input("Password: ")

username_benar = username == USERNAME_TERDAFTAR
password_benar = password == PASSWORD_TERDAFTAR

if username_benar:
    if password_benar:
        if akun_aktif:
            print("Login berhasil")
        else:
            print("Akun tidak aktif")
    else:
        print("Password salah")
else:
    print("Username salah")
