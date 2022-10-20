mots = 0
#ouvrir un fichier, second argument pour "r" read 
with open("data.txt", "r") as file:
    
#lis toutes les chaines de caracteres du fichier
    lignes = file.read()
#compte le nombre de "domain" 
    for n in lignes:
            mots += 1

print(mots)