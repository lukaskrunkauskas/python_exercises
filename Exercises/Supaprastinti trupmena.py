#Supaprastinti trupmeną a / b.
from fractions import Fraction

t_a = input()
inp = t_a.split(" ")
a, b = (int(inp[0]), int(inp[1]))
if a == 0:
    print(a, b)
else:
    sim_fraction = str(Fraction(a, b))
    temp = sim_fraction.split("/")
    print(" ".join(temp))
