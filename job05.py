input1 = int(input("Valeur 1 : "))
input2 = int(input("Valeur 2 : "))

for input1 in range(input1+1,input2) :
    print(input1)

for input1 in range(input1-1,input2,-1) :
    print(input1)
    
if input1 == input2:
    print("Valeurs égales")    