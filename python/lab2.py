# MEDII
#### Ex 1 -- Scrieți un program care să citească de la tastatură un număr natural n,
# să scrie într-un fișier n numere aleatorii între 1 și 1000 și să afișeze pe ecran maximul lor.

import random

x = int(input("Alege un numar: "))
f = open("Ex1.txt", 'w+')
for _ in range(x):
    number = str(random.randint(1, 1000))
    f.write(number)
    f.write('\n')
f.seek(0)
max = 1
for i in f.readlines():
    if int(i) > max:
        max = int(i)
    else:
        pass
print("Max number:", max)

# Exercitiul 2
# Medii
# Scrieți un program care să se execute cu două argumente (de tipul argv), care să fie un caracter și un fișier text,
# apoi să afișeze pe ecran de cîte ori apare caracterul respectiv în fișierul respectiv.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('c', help="Choose a letter")
parser.add_argument('f', help="Filename")

args = parser.parse_args()

char = args.c
filename = args.f
k = 0
with open(filename, "r") as f:
    for x in f.read():
        if x == char:
            k += 1

print(f"In {filename} we found {char} - {k} times ")

#### Ex 5 --- Scrieți un program care:
# se rulează cu 3 argumente numerice, a, b, n (exemplu $ python program.py 2 1023 2000);
# folosește un fișier de configurare JSON, care specifică numele și calea către un fișier de intrare, unul de ieșire și un interval de tipul [min, max];
# generează n numere naturale aleatorii între min și max și le scrie în fișierul de intrare;
# scrie în fișierul de ieșire numerele prime din fișierul de intrare, care se află între a și b;
# afișează pe ecran cel mai mare dintre aceste numere prime.

import argparse
import json
import random

parser = argparse.ArgumentParser()
parser.add_argument('n')
parser.add_argument('a')
parser.add_argument('b')

args = parser.parse_args()

a = int(args.a)
b = int(args.b)

js = open('config.json')

data = json.load(js)
prim = []

with open(data['input-file']['path'] + data['input-file']['name'], 'w+') as f1:
    for i in range(int(args.n)):
        number = str(random.randint(data['interval']['min'], data['interval']['max']))
        f1.write(number + '\n')
    f1.seek(0)
    for nb in f1.read().splitlines():
        if int(nb) > 1:
            for i in range(2, int(nb)):
                if (int(nb) % i) == 0:
                    break
            else:
                prim.append(nb)

if a > b:
    a, b = b, a
max = a
with open(data['output-file']['path'] + data['output-file']['name'], 'w+') as f2:
    for i in prim:
        if a < int(i) < b:
            f2.writelines(i + '\n')
            if max < int(i):
                max = int(i)
js.close()

print("Max number: ", max)

# Exercitiul 8
# Scrieți un program care generează un caracter aleatoriu c, apoi afișează pe ecran de cîte ori apare caracterul
# respectiv într-un text salvat într-un fișier de intrare (a) case sensitive (exemplu: dacă c = a, se afișează numărul
# de apariții ale lui a și numărul de apariții ale lui A) (b) case insensitive (se afișează suma aparițiilor
# caracterului cu minusculă și cu majusculă). Indicație: Puteți folosi o listă alfabet = ['a', 'b', 'c', 'd', ..., 'z']
# sau un string alfabet = "abcdefghijklmnopqrstuvwxyz" și generați un număr aleatoriu între 0 și 25, apoi preluați
# caracterul de pe poziția respectivă.
import random
import string

c = random.choice(string.ascii_letters.lower())
print(c)
low = 0
upp = 0
with open("Ex8.txt", 'r') as f:
    lines = f.read()
for i in lines:
    if c == i:
        low += 1
    elif c.upper() == i:
        upp += 1
print("Letter: " + c)
print(f"a) Case sensitive: {c} = {low} and {c.upper()} = {upp}")
print("b) Case nonsensitive: ", low + upp)

# Exercitiul 10
# Scrieți un program care scrie într-un fișier 10 numere aleatorii între 1 și 1000, apoi citește de la tastatură o
# opțiune s, d, p, c, pentru sumă, diferența, produs, cît și afișează într-un alt fișier calculul corespunzător:
# suma numerelor din primul fișier, diferența, produsul sau cîtul lor.
import random

ls = []

def calc(eq):
    with open('Ex10.txt', 'r') as f:
        for x in f.read().splitlines():
            ls.append(x)
        k = ls[0]
        for i in ls[1:]:
            q = str(k) + eq + i
            k = eval(q)
        return k


with open('Ex10.txt', 'w+') as f:
    for _ in range(10):
        f.write(str(random.randint(1, 1000)) + '\n')

print("""
    1. Suma
    2. Diferenta
    3. Produs
    4. Cat
    5. Exit
    """)

while True:
    rasp = int(input("Alege o optiune: "))

    if rasp == 1:
        print(calc("+"))
    elif rasp == 2:
        print(calc("-"))
    elif rasp == 3:
        print(calc("*"))
    elif rasp == 4:
        print(calc("/"))
    elif rasp == 5:
        print("Exit!")
        break
    else:
        print("Nu ai ales o optiune valida")