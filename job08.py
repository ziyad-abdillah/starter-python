hauteur = int(input("hauteur: "))
largeur = int(input("largeur: "))


for H in range(1,hauteur+1):
    for L in range(1,largeur+1):
        if (H == hauteur and L == largeur) or (L==1 and H==1):
            print("|", end="")
        elif L == 1 or L == largeur:
            print("|",end="")
        elif H == 1 or H == hauteur:
            print("-", end="")
        
        else:
            print(" ", end="")
    print("")