#Duoti keturi natūriniai skaičiai a, b, c ir d. Realizuoti programą, kuri skaičiuoja trupmenų a/b ir c/d sumą. Kitaip tariant reikia surasti, tokius x ir y, kad a/b+c/d=x/y, kur x/y – suprastinta trupmena.
from fractions import Fraction


def reduce(min_a, min_b):
    can_be_divided = True

    while can_be_divided:
        worked = False

        if min_a == 0:
            return min_a, min_b

        if min_a % min_b == 0:
            min_a /= min_b
            min_b = 1
            worked = False

        if min_b % min_a == 0:
            min_b /= min_a
            min_a = 1
            worked = False

        if min_a % 11 == 0 and min_b % 11 == 0:
            min_a /= 11
            min_b /= 11
            worked = True

        if min_a % 7 == 0 and min_b % 7 == 0:
            min_a /= 7
            min_b /= 7
            worked = True

        if min_a % 5 == 0 and min_b % 5 == 0:
            min_a /= 5
            min_b /= 5
            worked = True

        if min_a % 3 == 0 and min_b % 3 == 0:
            min_a /= 3
            min_b /= 3
            worked = True

        if min_a % 2 == 0 and min_b % 2 == 0:
            min_a /= 2
            min_b /= 2
            worked = True

        if not worked:
            can_be_divided = False

    return min_a, min_b


t_a = input()
inp = t_a.split(" ")
min_a, min_b, min_c, min_d = (int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3]))
sud_a = (min_d * min_a + min_b * min_c)
sud_b = (min_b * min_d)

sol_a, sol_b = reduce(int(sud_a), int(sud_b))

if sol_a == sol_b:
    print(1, 1)
else:
    sim_fraction = str(Fraction(int(sol_a), int(sol_b)))
    _temp = sim_fraction.split("/")
    last_temp = (" ".join(_temp))
    if len(last_temp) == 1:
        print(last_temp, 1)
    else:
        print(last_temp)
