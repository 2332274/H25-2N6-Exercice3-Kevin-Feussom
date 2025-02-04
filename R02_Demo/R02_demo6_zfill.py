
# liste d'éléments qui ne peuvent pas facilement être mis en ordre croissant
exemple = ["1-f00","2-barr","12-exemple"]

exemple.sort()
print(exemple)


# On veut modifier le début de chaque chaine de caractères pour qu'ils aient la même longueur.
newliste = []
for nom in exemple :
    num, nom = nom.split("-")
    num = num.zfill(2)
    newliste.append(f"{num}-{nom}")

newliste.sort()
print(newliste)