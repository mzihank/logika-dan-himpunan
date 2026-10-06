# 1. Variabel dan tipe data
nama = "Budi" # str
umur = 18 # int
ipk = 3.75 # float
mahasiswa_aktif = True # bool
print(nama, umur, ipk, mahasiswa_aktif)

# 2. Boolean
username_benar = True
password_benar = False

if username_benar:
    print("Username valid")
else:
    print("Username tidak valid")

# 3. Operator perbandingan
umur = 20
print(umur >= 17) # True
print(umur == 18) # False
print(umur != 20) # False
print(umur < 25) # True

nilai = 78
print(nilai >= 60) # True
print(nilai == 78) # True
print(nilai != 100) # True

# 4. Operator logika
p = True
q = False
print(p and q) # False
print(p or q) # True
print(not p) # False
print(p ^ q) # True (XOR)
print(p != q) # True (penulisan lain dari XOR)

# 5. Ekspresi logika majemuk: syarat lulus
nilai = 80
hadir = True
lulus = nilai >= 75 and hadir
print(lulus) # True

# 6. Sistem login: akun tidak aktif
username_benar = True
password_benar = True
akun_aktif = False

login = (
    username_benar and
    password_benar and
    akun_aktif
)

if login:
    print("Login berhasil")
else:
    print("Login gagal")

# 7. Pengujian 4 kondisi
uji = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (False, True, True),
]

print()
print("Username  Password  Aktif   Hasil")
for username, password, aktif in uji:
    hasil = username and password and aktif
    print(f"{str(username):<10}{str(password):<10}{str(aktif):<8}{hasil}")