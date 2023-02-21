#!/usr/bin/env python3
a = int(input("What is a: "))
b = int(input("What is b: "))
c = int(input("What is c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("The equation has no real roots.")
elif delta == 0:
    x = -b / (2*a)
    print("The equation has a single root: x =", x)
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("The equation has two roots: x1 =", x1, "and x2 =", x2)

# Find two numbers whose product is equal to a*c and sum is equal to b
for i in range(-abs(a*c), abs(a*c) + 1):
    for j in range(-abs(a*c), abs(a*c) + 1):
        if i * j == a * c and i + j == b:
            # Display the results and factorization of the trinomial
            print("The two numbers are", i, "and", j)
            print("Factorization of the trinomial:", a, "x^2 +", b, "x +", c, "=", a, "(x +", i/a, ")(x +", j/a, ")")
            break
    else:
        continue
    break
