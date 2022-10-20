nb = int(input("Nombre de lettres: "))
mots = 0
#ouvrir un fichier, second argument pour "r" read 
with open("data.txt", "r") as file:
    
#lis toutes les chaines de caracteres du fichier

    lignes = file.read()

#liste chaque mot dans une liste    
    liste = lignes.split()

#compte le nombre de mot si égal à l'entrée utilisateur 
    for n in liste:
        if len(n) == nb:
            mots += 1

print(mots)