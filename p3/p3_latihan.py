python2 = {"Ani", "Budi", "Citra"}
java2 = {"Budi", "Deni"}
sql2 = {"Ani", "Deni", "Eka"}
semua_mahasiswa = {"Ani", "Budi", "Citra", "Deni", "Eka", "Fajar"}

print("Python saja:", python2 - (java2 | sql2))
print("Python dan Java:", python2 & java2)
print("Minimal satu teknologi:", python2 | java2 | sql2)
print("Tidak menyukai ketiganya:", semua_mahasiswa - (python2 | java2 | sql2))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("B - A         :", B - A)
print("A & (B | A)   :", A & (B | A))
print("A - B == B - A:", A - B == B - A)
