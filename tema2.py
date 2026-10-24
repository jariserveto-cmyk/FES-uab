###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
#num1,num2 = input("Entra dos nombres:").split()
#if num1 > num2:
 #   print(f"{num1} es mes gran que {num2}")
#elif num1< num2:
 #   print(f"{num1} es mes petit que {num2}")
#else:
 #   print('Son iguals')

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
#num1,num2 = input("Entra dos nombres:").split()
#num1 = float(num1)
#num2 = float(num2)
#operacio = input("I una operacio(+,-,*,/):")
#if num2 == 0 and operacio == '/' :
 #   print("Error al dividir per 0")
#elif operacio == '+':
 #   suma = num1 + num2
  #  print(suma)
#elif operacio == '-':
 #   resta =num1 - num2
  #  print(resta)
#elif operacio == '*':
 #   producte= num1 * num2
  #  print(producte)
#elif operacio == '/':
 #   divisio= num1 / num2
  #  print(divisio)
#else:
 #   print('Operacio no trobada')    

###
# EXERCICIS
###

# Exercici 1: Comparar nombres
# Donats els nombres:
# nombre_a = 8
# nombre_b = 5
# Mostra el resultat de comparar si nombre_a és més gran, més petit o igual
# que nombre_b.
nombre_a =8
nombre_b = 5
print(nombre_a>nombre_b)
print(nombre_a<nombre_b)
print(nombre_a==nombre_b)

# Exercici 2: Comparar cadenes de text
# Donades les cadenes:
# paraula_a = "Hola"
# paraula_b = "hola"
# Mostra si són iguals i si paraula_a és igual a "Hola".
# Observa si Python distingeix entre majúscules i minúscules.
paraula_a = "Hola"
paraula_b = "hola"
print(paraula_a== paraula_b)
print(paraula_a=="Hola")
#Python si que ho distingueix