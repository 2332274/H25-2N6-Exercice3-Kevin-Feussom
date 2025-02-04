cours = ['Programmation 1', 'Math', 'Bureautique', 'Réseau 1','Math']
cours_optionnel = ['Education physique', 'Philosophie']
print(f"Liste au début : {cours}", end="\n\n")


# Ajouter le cours "Math" à la fin de la liste "cours" avec append()
cours.append("Math")


# Afficher le nombre de fois que le cours "Math" apparait
print(cours.count("Math"))

# Ajouter les cours "AI", "Systèmes" à la liste avec extend()
autre_cours = ["AI2","Systeme"]
cours.extend(autre_cours)

# Trouver l'index du cours "Bureautique" en utilisant index()
cours.index("Bureautique")
print( cours.index("Bureautique"))


# Ajouter un cours "BD2" après "Bureautique" en utilisant insert() avec l'index que nous venons de découvrir.
cours.insert(2, "BD2")

# Enlever le cours "AI" de la liste avec remove()
retourremove = cours.remove("AI2")

# Enlever le dernier item de la liste avec pop(). L'item enlevé est retourné par pop#
dernier_element = cours.pop()
print(cours)
print(dernier_element)
print()


# Ajouter les éléments de "cours_optionnel" à "cours" avec la méthode .extend()
# Attention à ne pas utilisé .append(), sinon on se retrouve avec une liste de listes
cours.extend(cours_optionnel)

# Vider la liste "cours_optionnel" avec la méthode clear().
# Imprimer le contenu de la liste.
cours_optionnel.clear()



# Mettre la lise de cours en ordre croissant avec sort()
# Puis metter la liste en ordre décroissant

cours.pop(4)
cours.sort()
cours.sort(reverse=True)

cours_2 = sorted(cours)

print(f"Liste Final : {cours}")





# Pour s'amuser, faisons une petite boucle qui permettra de retirer les duplicatas dans la liste "cours"

new_cours = []

for un_cours in cours :

    print (un_cours)
    if new_cours.count(un_cours) > 0
    
new_cours.append(un_cours)

