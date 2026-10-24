###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
num1,num2 = input("Entra dos nombres:").split()
if num1 > num2:
    print(f"{num1} es mes gran que {num2}")
elif num1< num2:
    print(f"{num1} es mes petit que {num2}")
else:
    print('Son iguals')
    

