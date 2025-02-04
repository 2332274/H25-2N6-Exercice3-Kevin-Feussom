auto_list = [ "ford" , "mustang" , 1964]

auto = {"marque":"ford",
        "modele": "mustange",
        "annee" : 1964}

# Obtenir l'année de fabrication avec le .get()
print(auto["annee"])
# Obtenir l'année de fabrication SANS le .get()
print(auto.get("annee"))


# Le comportement de auto["annee"] et auto.get["annee"] différent lorsque la clef n'existe pas 
# Essayons avec la couleur de la voiture
print(auto["modele"])

# Modifier l'année de fabrication pour que ce soit 1974
auto["anne"] = "1974"
auto["marque"]= "mercedes"
print(auto["anne"])
print(auto["marque"])

# Ajouter une valeur pour le kilomètrage
auto["kill"] = 12500000

auto.pop("kill")
annee_fabrication = auto.pop("annee")
print( len(auto))



print(auto)

for clef , valeur in auto.items():
      print(f" {clef} : {valeur}")


      