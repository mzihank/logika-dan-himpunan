# 1. Generator tabel kebenaran
nilai = [True, False]

print("P     Q     P and Q   P or Q   not P")
for p in nilai:
    for q in nilai:
        print(f"{p!s:<5} {q!s:<5} {p and q!s:<8} {p or q!s:<8} {not p!s}")

# 2. Fungsi implikasi dan biimplikasi
def implikasi(p, q):
    return (not p) or q

def biimplikasi(p, q):
    return implikasi(p, q) and implikasi(q, p)

print()
print(implikasi(True, True)) # True
print(implikasi(True, False)) # False
print(implikasi(False, True)) # True
print(implikasi(False, False)) # True

# 3. Pengembangan: tabel lima operator dengan fungsi terpisah
def operator_and(p, q):
    return p and q

def operator_or(p, q):
    return p or q

def operator_xor(p, q):
    return p ^ q

print()
print("P     Q     AND    OR     XOR    P->Q   P<->Q")
for p in nilai:
    for q in nilai:
        print(f"{p!s:<5} {q!s:<5} {operator_and(p, q)!s:<6} {operator_or(p, q)!s:<6} "
              f"{operator_xor(p, q)!s:<6} {implikasi(p, q)!s:<6} {biimplikasi(p, q)!s}")

# 4. Pengembangan: ekuivalensi dan hukum De Morgan
print()
print("P     Q     De Morgan I   De Morgan II   P->Q = (not P) or Q")
for p in nilai:
    for q in nilai:
        dm1 = (not (p and q)) == ((not p) or (not q))
        dm2 = (not (p or q)) == ((not p) and (not q))
        ek = implikasi(p, q) == ((not p) or q)
        print(f"{p!s:<5} {q!s:<5} {dm1!s:<13} {dm2!s:<14} {ek}")

# 5. Pengembangan: tautologi, kontradiksi, kontingensi
def klasifikasi(fungsi):
    hasil = [fungsi(p, q) for p in nilai for q in nilai]
    if all(hasil):
        return "tautologi"
    if not any(hasil):
        return "kontradiksi"
    return "kontingensi"

print()
print("P or not P         :", klasifikasi(lambda p, q: p or (not p)))
print("P and not P        :", klasifikasi(lambda p, q: p and (not p)))
print("P and Q            :", klasifikasi(lambda p, q: p and q))
print("(P or Q) and not P :", klasifikasi(lambda p, q: (p or q) and (not p)))

# 6. Kuantor universal dan eksistensial
mahasiswa = ["Andi", "Budi", "Citra"]
semua_punya_nama = all(len(x) > 2 for x in mahasiswa)
print()
print(semua_punya_nama) # True

daftar_nilai = [65, 80, 55, 90, 72]
ada_nilai_sempurna = any(x >= 90 for x in daftar_nilai)
print(ada_nilai_sempurna) # True

# 7. PBL seleksi peserta praktikum
def memenuhi_syarat(formulir, nilai, kehadiran, sanksi):
    return formulir and nilai >= 60 and kehadiran >= 75 and not sanksi

data = (True, 72, 80, False)
print()
print("Dapat mengikuti praktikum:", memenuhi_syarat(*data))

# Pengembangan: alasan penolakan
def alasan_penolakan(formulir, nilai, kehadiran, sanksi):
    alasan = []
    if not formulir:
        alasan.append("formulir belum diisi")
    if nilai < 60:
        alasan.append("nilai prasyarat kurang dari 60")
    if kehadiran < 75:
        alasan.append("kehadiran kurang dari 75%")
    if sanksi:
        alasan.append("terkena sanksi akademik")
    return alasan

print("Alasan penolakan:", alasan_penolakan(True, 55, 70, False))

# all() dan any() pada data nilai mahasiswa
nilai_mahasiswa = [72, 85, 60, 91, 58]
print("Semua nilai >= 60 :", all(n >= 60 for n in nilai_mahasiswa))
print("Ada nilai >= 90   :", any(n >= 90 for n in nilai_mahasiswa))

# 8. PBL modul PDF: Seleksi = (p ^ q ^ r) v s, 2^4 = 16 kombinasi
print()
print("p     q     r     s     Seleksi")
for p in nilai:
    for q in nilai:
        for r in nilai:
            for s in nilai:
                seleksi = (p and q and r) or s
                print(f"{p!s:<5} {q!s:<5} {r!s:<5} {s!s:<5} {seleksi}")
