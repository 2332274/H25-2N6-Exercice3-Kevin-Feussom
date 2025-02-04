# boucle for


liste_cours = ['Programmation 1', 'Math', 
               'Bureautique', 'Réseau 1','Math']

#print chacun des cours dans la liste
print (liste_cours)
for cours in liste_cours:
    print (f" {cours}")

    


#print chacun des cours dans la liste ansi que leur ( index + )
for nbr, cours in enumerate(liste_cours):
    print(f"Cours {nbr+1} : {cours}")


# Faire une boucle X fois avec la fonction range()