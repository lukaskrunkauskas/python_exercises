#Visi natūriniai skaičiai, pradedant nuo 1 užrašyti nuosekliai vienas po kito. Parašykite programą, kuri nustatytų, koks skaitmuo yra n-tojoje pozicijoje.
def listtostring(number_list):
    n_string = " "
    return (n_string.join(number_list))


n = int(input())

bad_chars = [",", " ", "[", "]"]
number_list = str(list(range(1, n + 1)))
number_string = listtostring(number_list)
for i in bad_chars:
    number_string = number_string.replace(i, "")
temp_string = number_string.strip()
print(temp_string[n - 1])
