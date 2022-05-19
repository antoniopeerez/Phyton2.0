<<<<<<< HEAD
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
print("Dime la medida de los catetos del triángulo")
cateto1 = int(input("cateto1: "))
cateto2 = int(input("cateto2: "))

hipotenusa = ((cateto1**2) + (cateto2**2)) **0.5

print ("La hipotenusa es", hipotenusa)
=======
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
#suma y la media de todos los números introducidos.

numero=(int)(input("Introduzca un numero y cuando desee acabar introduzca el 0 "))
suma=0
contador=0
while numero!=0:
    suma=suma+numero
    contador=contador+1
    numero=(int)(input("Introduzca un numero y cuando desee acabar introduzca el 0 "))

print("La media es",suma/contador)
print("La suma es ", suma)
>>>>>>> main
