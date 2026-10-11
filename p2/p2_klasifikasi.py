nilai = [True, False]

def klasifikasi(fungsi):
    hasil = [fungsi(p, q) for p in nilai for q in nilai]
    if all(hasil):
        return "tautologi"
    if any(hasil):
        return "kontingensi"
    return "kontradiksi"

print("P or (P ^ True)  :", klasifikasi(lambda p, q: p or (p ^ True)))
print("P and (P ^ True) :", klasifikasi(lambda p, q: p and (p ^ True)))
print("P and Q          :", klasifikasi(lambda p, q: p and q))
print("P or Q           :", klasifikasi(lambda p, q: p or q))
print("P ^ Q            :", klasifikasi(lambda p, q: p ^ q))
