python = {"Andi", "Budi", "Citra", "Dina"}
java = {"Budi", "Dina", "Eko"}
sql = {"Citra", "Dina", "Fajar"}
semua_mhs = {"Andi", "Budi", "Citra", "Dina", "Eko", "Fajar"}

python_saja = python - java - sql
python_java = python & java
minimal_satu = python | java | sql
tidak_ketiganya = semua_mhs - minimal_satu

print("Python saja     :", sorted(python_saja), len(python_saja))
print("Python dan Java :", sorted(python_java), len(python_java))
print("Minimal satu    :", sorted(minimal_satu), len(minimal_satu))
print("Tidak ketiganya :", sorted(tidak_ketiganya), len(tidak_ketiganya))

# Pengembangan: rumus inklusi-eksklusi
P, J, S = len(python), len(java), len(sql)
PJ = len(python & java)
PS = len(python & sql)
JS = len(java & sql)
PJS = len(python & java & sql)
print("Inklusi-eksklusi :", P + J + S - PJ - PS - JS + PJS)
print("len(union)       :", len(minimal_satu))
