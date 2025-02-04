# Q1                                                                                                                   #
# Créez une liste de 3 modèles de cartes graphiques. Voici une liste de cartes graphiques. Vous pouvez construire votre liste en choisissant parmi les suivantes:
#          GeForce RTX 3090Ti, GeForce RTX 3080Ti, GeForce RTX 3070Ti, Radeon RX 6950 XT, Radeon RX 6900 XT, Radeon RX 6800 XT             
# Vous pouvez aussi mettre un autre modèle de carte graphique si vous voulez.#
# imprimez la liste                                                                                                    #
print(f"Q1{u'_'*60}")

cartes_graphiques = [  "GeForce RTX 3090Ti", "GeForce RTX 3080Ti", "GeForce RTX 3070T" ]
print(f" Voici la liste des cartes graphiques que j'ai choisies : {cartes_graphiques}")



#Q2                                                                                                                   #
#  Obtenez la carte graphique à l'index 1 de la liste de vos cartes graphiques                                        #
#  Enlevez-la de la liste                                                                                             #
#  Imprimez la liste en spécifiant l'item enlevé                                                                      #
print(f"Q2{u'_'*60}")

index_a_1 = cartes_graphiques.pop(1)
print (index_a_1)
print(f"j'ai enlevé la carte graphique GeForce RTX 3080Ti. La liste est maintenant: {cartes_graphiques} ")



# Q3                                                                                                                   #
# Ajoutez un nouvel item à la fin de la liste                                                                          #
# et affichez la dernière carte graphique que vous avez maintenant dans la liste                                       #
print(f"Q3{u'_'*60}")

cartes_graphiques.append("Radeon RX 6800 XT" )
print (f" la nouvelle liste est : {cartes_graphiques}")


# Q4                                                                                                                 #
# Inversez les items de votre liste                                                                                  #
print(f"Q4{u'_'*60}")

inverse_2 = sorted(cartes_graphiques , reverse= True)
print (f" la liste inverse est : {inverse_2}")


# Q5                                                                                                                 #
# Créez une petite liste de deux nouvelles cartes graphiques                                                         #
# Imprimez cette nouvelle petite liste                                                                               #
# Ajoutez cette nouvelle petite liste à la fin de votre première liste                                               #
# Imprimez votre liste initale telle qu'elle est rendue                                                              #
print(f"Q5{u'_'*60}")

petite_liste = [ "AMD" , "NVIDIA"]
print(F" petite liste: {petite_liste}")
cartes_graphiques.extend(petite_liste)

print(f" la nouvelle liste avec la petit liste est : {cartes_graphiques}")


# Q6                                                                                                                  #
# Ordonnez la liste en ordre croissant de façon à créer une nouvelle liste                                            #
# et imprimez cette nouvelle liste                                                                                    #
print(f"Q6{u'_'*60}")

cartes_graphiques.sort()
print( f" la nouvelle liste en ordre croissant : {cartes_graphiques}")




