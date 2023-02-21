#!/usr/bin/env python3

a = int(input("Quel est le a : "))
b = int(input("Quel est le b : "))
c = int(input("Quel est le c : "))

# Trouver les deux nombres dont le produit est égal à a*c et la somme est égale à b
for i in range(-abs(a*c), abs(a*c) + 1):
    for j in range(-abs(a*c), abs(a*c) + 1):
        if i * j == a * c and i + j == b:
            # Afficher les résultats et la factorisation du trinôme
            print("Les deux nombres sont", i, "et", j)
            print("Factorisation du trinôme:", a, "x^2 +", b, "x +", c, "=", a, "(x +", i/a, ")(x +", j/a, ")")
            break
    else:
        #TODO: add 
        continue
    break
