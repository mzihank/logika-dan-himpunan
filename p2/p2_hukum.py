nilai = [True, False]

print("P     identitas AND   identitas OR   dominasi OR   dominasi AND")
for p in nilai:
    identitas_and = (p and True) == p
    identitas_or = (p or False) == p
    dominasi_or = (p or True) == True
    dominasi_and = (p and False) == False
    print(f"{p!s:<5} {identitas_and!s:<15} {identitas_or!s:<14} "
          f"{dominasi_or!s:<13} {dominasi_and}")
