#Duotas natūrinis skaičius n. Patikrinkite, ar tarp šio skaičiaus skaitmenų yra lygiai 3 vienodi. Jeigu tokių skaitmenų nėra, išveskite 0, jeigu tokių skaitmenų yra keli – išveskite juos per tarpą didėjimo tvarka.
#Išveskite surastus skaičius per tarpą, arba išveskite 0, jeigu tokių skaičių nėra.
from collections import Counter

n = list(input())
n_dic = (Counter(n))
final_list = []
for i in n_dic:
    if n_dic[i] == 3:
        final_list.append(i)

final_list.sort()
print(" ".join(final_list) if final_list else 0)
