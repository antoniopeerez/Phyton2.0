#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
print("Dime la medida de los catetos del triángulo")
cateto1 = int(input("cateto1: "))
cateto2 = int(input("cateto2: "))

hipotenusa = ((cateto1**2) + (cateto2**2)) **0.5

print ("La hipotenusa es", hipotenusa)