<<<<<<< HEAD
#Calcular el perímetro y área de un rectángulo dada su base y su altura
print("indica la medida de los lados del triangulo")
lado1 = int(input("lado1: "))
lado2 = int(input("lado2: "))
lado3 = int(input("lado3: "))

print("indica la medida de la base y de la altura del triangulo")
base = int(input("base: "))
altura = int(input("altura: "))

perimetro = lado1 + lado2 + lado3
altura = base*altura/2
print("El perimetro es", perimetro, "y la base es", base)
=======
#Crea una aplicación que permita adivinar un número. La aplicación genera un
#número aleatorio del 1 al 100. A continuación va pidiendo números y va
#respondiendo si el número a adivinar es mayor o menor que el introducido,a
#demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
#programa termina cuando se acierta el número (además te dice en cuantos
#intentos lo has acertado), si se llega al limite de intentos te muestra el número
#que había generado.


import random

intentos=0

numero=random.randint(1,100)
print('Estoy pensando en un numero entre el 1 y el 100 intente adivinarlo en 10 intentos')

while intentos<10:
    adivina=input()
    adivina=(int)(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡Demasiado pequeño! Intentelo de nuevo.')

    if adivina>numero:
        print('¡Demasiado grande! Intentelo de nuevo.')

    if adivina==numero:
        break

if adivina==numero:
    intentos=str(intentos)
    print('Acertaste el número en '+intentos+' intentos. !')

if adivina!=numero:
    numero=str(numero)
    print(' Yo estaba pensando en el número '+numero+".Lo siento.")
>>>>>>> main
