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
