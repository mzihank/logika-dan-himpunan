def operator_and(p, q):
    return p and q

def operator_or(p, q):
    return p or q

def operator_xor(p, q):
    return p ^ q

nilai = [True, False]

print("P     Q     AND    OR     XOR")
for p in nilai:
    for q in nilai:
        print(f"{p!s:<5} {q!s:<5} {operator_and(p, q)!s:<6} "
              f"{operator_or(p, q)!s:<6} {operator_xor(p, q)!s}")
