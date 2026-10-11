username_benar = True
password_benar = True
akun_aktif = False

login = username_benar and password_benar and akun_aktif

if login:
    print("Login berhasil")
else:
    print("Login gagal")

uji = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (False, True, True),
]

print()
print("Username  Password  Aktif   Hasil")
for p, q, r in uji:
    hasil = p and q and r
    print(f"{str(p):<10}{str(q):<10}{str(r):<8}{hasil}")
