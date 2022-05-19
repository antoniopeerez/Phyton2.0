<<<<<<< HEAD
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
print("Dime dos numeros")
numero1 = int(input("numero1: "))
numero2 = int(input("numero2: "))
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

print("La suma de estos dos numero es", suma, "la resta de estos dos numeros es", resta, "la multiplicacion de estos dos numeros es", multiplicacion, "y la division de estos dos numeros es", division )
=======
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
#números a introducir). El programa debe informar de cuantos números
#introducidos son mayores que 0, menores que 0 e iguales a 0.
ig=0
may=0
men=0

cant=int(input("Introduzca la cantidad de numeros que quiere introducir"))

for i in range (0,cant):
    numero=int(input("Introduzca un numero "))
    if numero==0:
     ig=ig+1
    if numero<0:
     men=men+1
    if numero>0:
     may=may+1   
print("Has introducido ",ig,"0, ", may," numeros mayor es de 0 y ",men," numeros menores de 0")
>>>>>>> main
