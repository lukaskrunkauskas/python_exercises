#ntervale [n, m] surasti visus skaičius-palindromus, kurių kvadratai irgi yra skaičiai-palindromai.
#Išveskite surastus skaičius-palindromus vienoje eilutėje per tarpus. Jeigu duotame intervale nėra nei vieno sąlygą atitinkančio skaičiaus – išveskite 0.
inp = input()
inp_split = inp.split(" ")
n = int(inp_split[0])
m = int(inp_split[1])
ats = []

for i in range(n, m + 1):
    temp = str(i)
    if temp[::-1] == temp:
        temp_square = str(i * i)

        if temp_square[::-1] == temp_square:
            ats.append(temp)
if not ats:
    print(0)
else:
    print(' '.join(map(str, ats)))
