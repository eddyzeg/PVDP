# Sectiunea 1
# Exercitiul 1
#
# 1.1. (0.5p) Scrieți un program care să primească de la tastatură unul dintre prenumele dumneavoastră și
# să afișeze două șiruri de caractere, unul alcătuit doar din vocalele din prenume, iar celălalt alcătuit
# doar din consoanele din prenume. Includeți și condițiile corespunzătoare de validare a datelor de intrare.
# Exemplu: Pentru "Adrian", se afișează "aia" și "drn".

name = input("Name: ")
vowels = ['a', 'e', 'i', 'o', 'u']
n1, n2 = '', ''
for i in name.lower():
    if i in vowels:
        n1 += i
    else:
        n2 += i

print(n1, n2)

# Exercitiul 2

# 1.2. (0.5p) Scrieți un program care să primească drept date de intrare z, l, a, unde z este ziua
# dumneavoastră de naștere, l este luna și a este anul și să afișeze descompunerea în factori primi a
# produsului lor. Includeți și condițiile corespunzătoare de validare a datelor de intrare.
#
# Exemplu: Pentru z = 5, l = 11, a = 1999, se afișează 109945 = 5^1 * 11^1 * 1999^1.


def factor(n):
    detailed = ''
    f = 2
    sum = 1
    while n > 1:
        p = 0
        while n % f == 0:
            n = n / f
            p += 1
            if p > 0:
                detailed += f"({f}^{p}) * "
                sum = sum * (f ^ p)
        f += 1
    detailed = detailed[:-2]
    return detailed, sum


print("Insert your birthday")
birthday = {
    "Day": {
        'min': 1,
        'max': 31
    },
    "Month": {
        'min': 1,
        'max': 12
    },
    "Year": {
        'min': 1900,
        'max': 2022
    }
}
ls = []
sum = ''
total = 1
for _ in birthday.keys():
    x = int(input(_ + ": "))
    if x in range(birthday[_]['min'], birthday[_]['max']):
        a, b = factor(x)
        sum += a + "* "
        total += total * b
    else:
        print(f"Wrong type, need to be in interval [{birthday[_]['min']} - {birthday[_]['max']}]")

sum = sum[:-2]

print(str(sum) + " = " + str(total))

# 1.3. (0.5p) Scrieți un program care să primească de la tastatură n și k și să calculeze combinări de n luate cîte k.
# Includeți și condițiile corespunzătoare de validare a datelor de intrare.

n = int(input("n: "))
k = int(input("k: "))


def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


if n >= k:
    n_fact = fact(n)
    k_fact = fact(k)
    l_fact = fact(n - k)
    print(n_fact / (k_fact * l_fact))
else:
    print("Wrong input!")

# 1.4. (0.5p) Scrieți un program care să citească un text dintr-un fișier (exemplu: un articol de pe Wikipedia)
# și unul dintre prenumele dumneavoastră de la tastatură și să afișeze de cîte ori apare în text fiecare literă
# din prenume, ținînd cont de majusculă/minusculă (i.e. apariția lui "a" este diferită de apariția lui "A").

n = input("Insert your name and last name: ")
print(n)
q = 0
letter = []
with open("ex 4.txt", 'r') as f:
    for j in n.replace(" ", ""):
        if j not in letter:
            for i in f.read().replace(" ", ""):
                if i == j:
                    q += 1
            print(str(j) + " --> "+ str(q))
            letter.append(j)
            q = 0
            f.seek(0)

# Exercitiul 6
# 6. (1p) Scrieți un program care să primească de la tastatură un număr natural n > 2 și să afișeze toate
# submulțimile mulțimii {1, 2, 3, ..., n}. Exemplu: n = 3, se afișează {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}.
# Includeți și condițiile corespunzătoare de validare a datelor de intrare.

import itertools

ok = True
while ok:
    n = int(input("n: "))
    if n > 2:
        ok = False
    else:
        print("Choose a mumber > 2")

ls = []
for i in range(1, n + 1):
    ls.append(i)

z = 1
y = ''
while z <= n:
    for x in (itertools.combinations(ls, z)):
        y += str(x).replace("(", "{").replace(")", "}").replace(",","") + ', '
    z += 1

print(y[:-2])

# Exercitiul 7

# 1.7. (1p) Scrieți un program care să citească de la tastatură n, care reprezintă anul nașterii dumneavoastră și să
# genereze aleatoriu o listă de n numere naturale, cu valori între luna nașterii și ziua de naștere.
# Afișați media numerelor generate și ce procent din numărul de numere generate este mai mare decît media.
import random

n = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))

if m > d:
    m, d = d, m

numbers = []
for _ in range(n):
    numbers.append(random.randint(m, d))

k = 0
med = sum(numbers) / n
for i in numbers:
    if i > med:
        k += 1
print(numbers)
result = (100 / n) * k
result = "{:.2f}".format(result)

print(result + "%")