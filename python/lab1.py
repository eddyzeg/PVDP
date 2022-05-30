#problema 1
l=[9,11,6,21,0,7,28,30,12,17]
l1=[]#in l1 vom retine cifrele numarului eliminand cifrele de pe pozitii impare
for i  in range(len(l)):
  if i%2!=0:
   l1.append(l[i])
print(l1)

#problema 2
#definim doua liste in carea retinem cifrele numerelor
s=[1,2,3,4,5]
s1=[2,4,6,8,0]
s2=[]
for i in range(5):
 s2.append(s[i])
 s2.append(s1[i])
print(s2)
#problema 3
j=[1,2,8,9,0,7,4,7,8]
n=eval(input("introduceti pozitia cifrei"))
for i in range(len(j)):
 if i==n:
  print("cirfra de pe pozitia introdusa de la tastatura este", j[i-1])
#problema 4
m=eval(input("introduceti numarul de la tastatura"))
for i in range(0,m+1):
 if i%2!=0:
  print(i, end=',')
#problema 5
p=eval(input( "introduceti primul numar"))
q=eval(input("introduceti al doilea numar"))
k=0
for i in range(p,q+1):
 if i%2!=0 and i%5!=0:
  print(i, end=',')
  k+=1
print()
print(k)

### Medii
# -- Problema 7 ###
# Listă de invitați: Scrieți un program care alcătuiește o listă de invitați, cu următorii pași:
## se citește mai întîi lista de persoane pe care NU le vrem invitate ("lista neagră")
## se citesc apoi invitații;
## se respinge un invitat dacă este pe "lista neagră";
## se respinge un nume dacă a mai fost deja invitat;
## se adaugă invitați pe listă pînă la introducerea unui caracter special (de exemplu, q de la quit sau x de la exit);
## se afișează lista finală de invitați permiși

with open('BlackList.txt') as f:
    names = f.read()
    black_list = names.split(',')
invitation_list = []
while True:
    guests = input("Enter a name of your guest: ")
    if guests == 'e' or guests == 'q':
        break
    else:
        if guests in black_list:
            print("Rejected! This guest is blacklisted")
        elif guests in invitation_list:
            print("This guest has already been added")
        else:
            invitation_list.append(guests)

print(" The Guest List:", ', '.join(invitation_list))

# -- Problema 10 ###
# Scrieți un program care citește de la tastatură două perechi de numere reale, (x1, y1) și (x2, y2)
# și afișează lungimea segmentului determinat de cele două puncte.
# Formula de calcul este sqrt((x1 - x2)^2 + (y1 - y2)^2).
import math

x1, y1 = eval(input("x1 and y1 for A:"))
x2, y2 = eval(input("x2 and y2 for B:"))

print(f'A{(x1, y1)}      B{(x2, y2)}')

print("Result:", math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))