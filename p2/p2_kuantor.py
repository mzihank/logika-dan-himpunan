mahasiswa = ["Andi", "Budi", "Citra"]
semua_punya_nama = all(len(x) > 2 for x in mahasiswa)
print(semua_punya_nama)   # True

daftar_nilai = [65, 80, 55, 90, 72]
ada_nilai_sempurna = any(x >= 90 for x in daftar_nilai)
print(ada_nilai_sempurna)   # True

nilai_mahasiswa = [72, 85, 60, 91, 58]
print("Semua nilai >= 60 :", all(n >= 60 for n in nilai_mahasiswa))
print("Ada nilai >= 90   :", any(n >= 90 for n in nilai_mahasiswa))

# Seleksi peserta
def memenuhi_syarat(formulir, nilai, kehadiran, bebas_sanksi):
    return formulir and nilai >= 60 and kehadiran >= 75 and bebas_sanksi

data = (True, 72, 80, True)
print("Dapat mengikuti praktikum:", memenuhi_syarat(*data))
