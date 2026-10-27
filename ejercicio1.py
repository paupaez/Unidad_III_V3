print("------- Clasificador de triangulos -------")
print("A continuacion, ingresaras los valores del los lados del triangulo: ")

lado_a = float(input("Ingresa el valor del lado A: "))
while lado_a <= 0:
    lado_a = float(input("El valor es invalido (debe ser positivo), por favor, ingresa nuevamente el valor del lado A: "))

lado_b = float(input("Ingresa el valor del lado B: "))
while lado_b <= 0:
    lado_b = float(input("El valor es invalido (debe ser positivo), por favor, ingresa nuevamente el valor del lado B: "))

lado_c = float(input("Ingresa el valor del lado C: "))
while lado_c <= 0:
    lado_c = float(input("El valor es invalido (debe ser positivo), por favor, ingresa nuevamente el valor del lado C: "))

if (lado_a + lado_b > lado_c) or (lado_a + lado_c > lado_b) or (lado_b + lado_c > lado_a):
    print("Los lados ingresados si forman un triangulo válido")

    if (lado_a == lado_b == lado_c):
        print("Tipo de triangulo: Equilatero")

    elif (lado_a == lado_b) or (lado_a == lado_b) or (lado_b == lado_c):
        print("Tipo de triangulo: Isósceles")

    else:
        print("Tipo de triangulo: Escaleno")

else:
    print("Los lados ingresados no forman un triangulo")