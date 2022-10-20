droite = "\\"
gauche = "/"
bas = "__"

hauteur = int(input("hauteur: "))

for i in range(hauteur):
    print((hauteur - i) * " " + gauche + ((i * 2) * " ") + droite)
    if i == hauteur - 1:
        print(gauche + bas * hauteur + droite)