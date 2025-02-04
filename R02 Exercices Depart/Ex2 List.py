# Q1                                                                                                                   #
# Créez une liste de 3 barrettes de RAM parmi les suivantes:                                                          #
#          G.SKILL Trident Z5, CORSAIR Dominator, CORSAIR Vengeance, G.SKILL Ripjaws V, G.SKILL Ripjaws X              #
# imprimez la liste                                                                                                    #
print(f"Q1{'_'*60}")

barrettes = [ "G.SKILL Trident Z5" , "CORSAIR Dominator" , "CORSAIR Venegeance" ,"G.SKILL Ripjaws V", "G.SKILL Ripjaws X"]

print (f"Voici la liste : {barrettes}")


# Q2                                                                                                                   #
# Ajoutez un item à la fin de la liste avec append                                                                     #
# et affichez la dernière barrette RAM que vous avez dans la liste                                                     #
print(f"Q2{'_'*60}")

barrettes.append("AIR CANADA")
print(F"la derniere barette RAM ajoutée récemment est : {barrettes[-1]}")







#  Q3                                                                                                               #
#  Observez quelle est la deuxième barrette de RAM de votre liste                                                   #
#  Enlevez-la de la liste avec remove                                                                               #
#  Imprimez la liste en spécifiant la barrette de RAM enlevée                                                       #
print(f"Q3{'_'*60}")

barrettes.remove("CORSAIR Dominator")
print( f" la barrette enlevée est CORSAIR Dominator et la nouvelle liste est:{barrettes}")





# Q4                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
print(f"Q4{'_'*60}")

barrettes.sort()
print(f" Voici la liste en ordre croissant : {barrettes}")




# Q5                                                                                                             #
# Crée une nouvelle liste en ordre décroissant avec la fonction sorted (qui prend la liste originel en paramètre)                    #
# et imprimez-la                                                                                                 
print(f"Q5{'_'*60}")

barrettes.sort(reverse = True)
sorted(barrettes)
print(f" la nouvelle liste en ordre decroissant : {barrettes}")



# Q6                                                                                                                 #
# Imprimez le nombre d'éléments qu'il y a dans votre liste présentement                                              #
print(f"Q6{u'_'*60}")







# Q7                                                                                                                 #
# Imprimez une sous-liste des deux dernières barrettes RAMS de votre liste, en utilisant le slicing                  #
print(f"Q7{u'_'*60}")

print( barrettes[3:])




