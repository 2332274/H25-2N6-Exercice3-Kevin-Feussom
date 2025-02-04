import csv
#Nous avons une liste d'étudiants. 
liste_etudiants = [ ["Anna",543564,"420-INFO"],
                    ["Greg",987123,"420-INFO"],
                    ["Bob",369852,"238-FRAN"],
                    ["Joseph",753869,"135-PHYS"],
                    ["Hubert",125478,"238-FRAN"],
                    ["Zeus",659327,"135-PHYS"],
                    ["Joel",583649,"420-INFO"] ]


with open("etudiants_ids.csv", "w" , encoding="utf-8") as fichier_csv :
    writer = csv.writer(fichier_csv , lineterminator="\n")
    writer.writerow(["Nom" , "ID" , "Prog"])
    for etudiant in liste_etudiants:
        writer.writerow(etudiant)



with open("etudiants_ids.csv", "r" , encoding= "utf-8") as fichier_lu :
    reader = csv.reader(fichier_lu,delimiter=",")
    for ligne in reader:
      print(ligne)
if ligne