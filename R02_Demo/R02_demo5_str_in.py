# Liste de cours sous forme de chaine de caractères
infos = "Prog2-réseautique Scripting-sous-Linux Réseautique Introduction-base-de-données"


# Est-ce qu'un des cours traite de linux ?
# On peut utilisé la méthode .find(), la méthode .index() ou le mot-clef "in"
print (infos.find("linux"))
print(infos.index("Linux"))
print ("linux" in infos.lower())


# Transformer la variable infos en une liste utilisable
infos_list = infos.split(" ")




# Est-ce qu'un cours de cette liste traite de linux ?
print ("linux" in infos_list)


for cours in infos_list:
    print ("linux" in cours.lower()) 



# Liste de professeurs du département.
professeurs = ["  Chantal vallières ", "Pierre-Paul gallant  ", "Vincent carrier", "Joris   Deguet"]

# Pour rendre cette liste utilisable, on veut retirer les espaces superflues.
for prof in professeurs:
    nom_complet = prof.strip()
prenom , nom = nom_complet.split()
print (f" { prenom.capitalize()} {nom.capitalize()}")
# On veut aussi mettre le prénom et le nom de famille avec une majuscule.
