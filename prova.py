# Exercici 1
# Imprimeix el teu nom i cognom a la consola
print("Jari Serveto")
# Exercici 2
# Imprimeix les paraules "Python", "és", "divertit" separades per un guió (-)
# Pista: utilitza el paràmetre 'sep' de print()
print("Python","és","divertit",sep = "-")
# Exercici 3
# Imprimeix el resultat de la suma 15 + 27
print(15+27)
# Exercici 1
# Imprimeix el tipus del número 25


print(type(25))
# Exercici 2
# Imprimeix el tipus del text "Hola món"


print(type("Hola mon"))
# Exercici 3
# Imprimeix el tipus del resultat de la comparació 10 > 5
print(type(10>5))print(type(10>5))

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
numero_paquets = int(input("Numero de paquets rebuts pel encaminador"))
total_paquets = numero_paquets + 1200
print(f"Total de paquets:{total_paquets}")
# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_connexio = float(input("Velocitat de la connexio en mbps:"))
velocitat_segon = velocitat_connexio / 8
print(f"Velocitat per segon:{velocitat_segon.2f}MB/s")