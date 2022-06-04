f1 = open("text.txt", "r", encoding='utf-8')
a = open("Arts_spectacle.txt", "a", encoding='utf-8')
b = open("Enseignement_éducation.txt", "a", encoding='utf-8')
c = open("Environnement_tourisme.txt", "a", encoding='utf-8')
d = open("Histoire.txt", "a", encoding='utf-8')
e = open("Littérature.txt", "a", encoding='utf-8')
f = open("Nouvelles_technologies.txt", "a", encoding='utf-8')
g = open("Politique.txt", "a", encoding='utf-8')
h = open("Société_économie.txt", "a", encoding='utf-8')

for x in f1:
    print(x)
    n = int(input("Section"))
    while(n <= 0 or n >= 9):
        n = int(input("invalid"))
    if (n == 1): a.write(x)
    if (n == 2): b.write(x)
    if (n == 3): c.write(x)
    if (n == 4): d.write(x)
    if (n == 5): e.write(x)
    if (n == 6): f.write(x)
    if (n == 7): g.write(x)
    if (n == 8): h.write(x)





