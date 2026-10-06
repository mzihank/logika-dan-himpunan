nilai = [True, False]

def cetak_tabel(judul, kolom, fungsi):
    k1, k2, k3 = kolom
    print(judul)
    print(f"{k1:<12}{k2:<12}{k3:<12}Hasil")
    for a in nilai:
        for b in nilai:
            for c in nilai:
                print(f"{str(a):<12}{str(b):<12}{str(c):<12}{fungsi(a, b, c)}")
    print()

# Kasus AND
def seleksi_lulus(aktif, nilai_ok, prasyarat):
    return aktif and nilai_ok and prasyarat

# Kasus OR
def dapat_masuk(email, nomor_hp, akun_google):
    return email or nomor_hp or akun_google

# Kasus XOR
def metode_masuk(google, github, email):
    return google ^ github ^ email

cetak_tabel("Kasus AND: seleksi lulus", ("Aktif", "Nilai", "Prasyarat"), seleksi_lulus)
cetak_tabel("Kasus OR: dapat masuk", ("Email", "Nomor HP", "Google"), dapat_masuk)
cetak_tabel("Kasus XOR: metode masuk", ("Google", "GitHub", "Email"), metode_masuk)