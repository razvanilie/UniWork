# Se dă un graf neorientat conex cu n>3 vârfuri și m>n muchii.
# Informațiile despre graf se citesc din fișierul graf.in cu următoarea structură:
# - pe prima linie sunt n și m
# - pe următoarele m linii sunt câte 2 numere naturale reprezentând extremitățile unei
# muchii
# Se citește de la tastatură un vârf v.
# a) Să se afișeze muchiile critice care sunt incidente în v, dacă există (altfel se va afișa mesajul
# “nu exista”). O(m)
# b) Să se afișeze listele de adiacență ale unui arbore parțial T al lui G în care vârful v are
# gradul cu 1 mai mic decât îl are în G: dT(v) = dG(v) – 1, dacă un astfel de arbore există O(m)

f = open('graf.in', 'r')
firstline = f.readline()
n = int(firstline.split()[0])
m = int(firstline.split()[1])
for x in f.readlines():
    