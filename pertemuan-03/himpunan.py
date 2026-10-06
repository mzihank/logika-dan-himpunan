from itertools import product

# 1. Operasi himpunan dengan set Python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
U = set(range(1, 9))

print("Union       :", A | B)
print("Intersection:", A & B)
print("Difference  :", A - B)
print("Complement  :", U - A)
print("Cardinality :", len(A))
print("Subset?     :", A <= U)
print("A x B       :", set(product(A, B)))

# 2. Difference dan symmetric difference
print()
print(A - B)  # {1, 2}
print(B - A)  # {5, 6}
print(A ^ B)  # {1, 2, 5, 6}

# 3. PBL preferensi teknologi mahasiswa
python = {"Andi", "Budi", "Citra", "Dina"}
java = {"Budi", "Dina", "Eko"}
sql = {"Citra", "Dina", "Fajar"}

semua_mhs = {"Andi", "Budi", "Citra", "Dina", "Eko", "Fajar"}

python_saja = python - java - sql
python_java = python & java
minimal_satu = python | java | sql
tidak_ketiganya = semua_mhs - minimal_satu

print()
print("Python saja     :", sorted(python_saja), len(python_saja))
print("Python dan Java :", sorted(python_java), len(python_java))
print("Minimal satu    :", sorted(minimal_satu), len(minimal_satu))
print("Tidak ketiganya :", sorted(tidak_ketiganya), len(tidak_ketiganya))

# Eksplorasi lanjutan modul PDF: rumus inklusi-eksklusi
P, J, S = len(python), len(java), len(sql)
PJ = len(python & java)
PS = len(python & sql)
JS = len(java & sql)
PJS = len(python & java & sql)
inklusi_eksklusi = P + J + S - PJ - PS - JS + PJS
print("Inklusi-eksklusi :", inklusi_eksklusi)
print("len(union)       :", len(python | java | sql))

# 4. PBL preferensi teknologi mahasiswa, data modul zip
python2 = {"Ani", "Budi", "Citra"}
java2 = {"Budi", "Deni"}
sql2 = {"Ani", "Deni", "Eka"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Deni", "Eka", "Fajar"}

python_saja2 = python2 - (java2 | sql2)
python_dan_java = python2 & java2
minimal_satu2 = python2 | java2 | sql2
tidak_menyukai_ketiganya = semua_mahasiswa - (python2 | java2 | sql2)

print()
print("Python saja:", python_saja2)
print("Python dan Java:", python_dan_java)
print("Minimal satu teknologi:", minimal_satu2)
print("Tidak menyukai ketiganya:", tidak_menyukai_ketiganya)

# 5. Latihan
print()
print("B - A         :", B - A)
print("A & (B | A)   :", A & (B | A))
print("A - B == B - A:", A - B == B - A)