domains = 0
#ouvrir un fichier, second argument pour "r" read 
with open("domains.xml", "r") as file:
#lis toutes les lignes du fichier
    lignes = file.readlines()
#compte le nombre de "domain" 
    for n in lignes:
        if '"domain"' in n:
            domains += 1

print(domains)