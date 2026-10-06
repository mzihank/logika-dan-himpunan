# 1. Implementasi sistem seleksi
aktif = True
nilai_memenuhi = True
prasyarat = True
pengalaman = False
sertifikat = True

# Model logika
lulus = aktif and nilai_memenuhi and prasyarat
prioritas = pengalaman or sertifikat

# Output hasil seleksi
if lulus:
    print("Peserta LULUS seleksi")
else:
    print("Peserta TIDAK LULUS seleksi")

if prioritas:
    print("Peserta mendapat PRIORITAS")
else:
    print("Peserta tidak mendapat prioritas")

# 2. Matriks pengujian syarat dasar
skenario = [
    (True,  True,  True,  "LULUS"),
    (True,  True,  False, "TIDAK LULUS"),
    (True,  False, True,  "TIDAK LULUS"),
    (False, True,  True,  "TIDAK LULUS"),
    (False, False, False, "TIDAK LULUS"),
]

print()
print("Aktif  Nilai  Prasyarat  Expected     Actual       Status")
for a, n, pr, expected in skenario:
    hasil = a and n and pr
    actual = "LULUS" if hasil else "TIDAK LULUS"
    status = "PASS" if actual == expected else "FAIL"
    print(f"{str(a):<7}{str(n):<7}{str(pr):<11}{expected:<13}{actual:<13}{status}")

# 3. Starter code seleksi pelatihan
peserta = [
    {"nama": "Ani", "aktif": True, "nilai": 80, "kehadiran": 90,
     "sanksi": False, "teknologi": {"Python"}},
    {"nama": "Budi", "aktif": True, "nilai": 59, "kehadiran": 88,
     "sanksi": False, "teknologi": {"SQL"}},
    {"nama": "Citra", "aktif": True, "nilai": 75, "kehadiran": 75,
     "sanksi": False, "teknologi": {"Java"}},
    {"nama": "Deni", "aktif": False, "nilai": 90, "kehadiran": 95,
     "sanksi": False, "teknologi": {"Python", "SQL"}},
]

def lolos(data):
    return (
        data["aktif"]
        and data["nilai"] >= 60
        and data["kehadiran"] >= 75
        and not data["sanksi"]
        and bool(data["teknologi"] & {"Python", "SQL"})
    )

print()
for data in peserta:
    print(data["nama"], "lolos" if lolos(data) else "tidak lolos")

# 4. Pengembangan: 8 test case, termasuk nilai 60 dan kehadiran 75 (batas)
#    Expected ditentukan dari model, bukan dari program.
uji = [
    ("TC1 semua syarat terpenuhi", True, 80, 90, False, {"Python"}, True),
    ("TC2 nilai tepat 60 (batas)", True, 60, 80, False, {"SQL"}, True),
    ("TC3 kehadiran tepat 75 (batas)", True, 70, 75, False, {"Python"}, True),
    ("TC4 nilai 59 (di bawah batas)", True, 59, 90, False, {"Python"}, False),
    ("TC5 kehadiran 74 (di bawah batas)", True, 80, 74, False, {"SQL"}, False),
    ("TC6 status tidak aktif", False, 90, 95, False, {"Python"}, False),
    ("TC7 terkena sanksi", True, 85, 90, True, {"Python"}, False),
    ("TC8 hanya menyukai Java", True, 85, 90, False, {"Java"}, False),
]

print()
print(f"{'Test case':<36}{'Expected':<10}{'Actual':<10}Status")
for nama_tc, a, n, k, s, t, expected in uji:
    data = {"aktif": a, "nilai": n, "kehadiran": k, "sanksi": s, "teknologi": t}
    actual = lolos(data)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{nama_tc:<36}{str(expected):<10}{str(actual):<10}{status}")

# 5. Pengembangan: model himpunan
A = {"Andi", "Budi", "Citra", "Dina"}
B = {"Andi", "Budi", "Citra", "Eko"}
C = {"Andi", "Citra", "Dina", "Eko"}
D = {"Citra", "Fajar"}
E = {"Andi", "Dina"}

seleksi = A & B & C
prior = D | E
terbaik = (A & B & C) & (D | E)

print()
print("Seleksi :", sorted(seleksi))
print("Prior   :", sorted(prior))
print("Terbaik :", sorted(terbaik))