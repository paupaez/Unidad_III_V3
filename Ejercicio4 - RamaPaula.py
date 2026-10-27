import math


while True:

    print("------- Calculadora geométrica -------")
    print("1. Area de un circulo")
    print("2. Calculo de hipotenusa")
    print("3. Resolver una ecuacion cuadratica")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))
    
    match opcion:
        case 1:
            print("--- Area de un circulo ---")
            radio = float(input("Ingresa el valor del radio: "))
            area = math.pi * (radio ** 2)
            print(f"El area del círculo es: {area}")

        case 2:
            print("--- Hipotenusa de un triangulo rectangulo ---")

            cateto_a = float(input("Ingresa el valor del cateto A: "))
            while cateto_a <= 0:
                cateto_a = float(input("El valor ingresado debe ser positivo. Por favor, vuelve a ingresar el valor del cateto A: "))

            cateto_b = float(input("Ingresa el valor del cateto B: "))
            while cateto_b <= 0:
                cateto_b = float(input("El valor ingresado debe ser positivo. Por favor, vuelve a ingresar el valor del cateto B: "))

            hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b **2 )
            print(f"La hipotenusa del triangulo es: {hipotenusa}")

        case 3:
            print("--- Ecuacion cuadrática ---")
            print("Ingresa los coeficientes de la ecuacion: ")
            coe_a = float(input("Ingresa el coeficiente a: "))
            coe_b = float(input("Ingresa el coeficiente b: "))
            coe_c = float(input("Ingresa el coeficiente c: "))

            if coe_a == 0:
                print("Esta no es una ecuacion cuadrática")
            else:
                determinante = coe_b ** 2 - 4 * coe_a * coe_c

                if determinante > 0:
                    x1 = (- coe_b + math.sqrt(determinante)) / 2 * coe_a
                    x2 = (- coe_b - math.sqrt(determinante)) / 2 * coe_a
                    print(f"Primera solucion: {x1}")
                    print(f"Segunda solucion: {x2}")

                elif determinante == 0:
                    x1 = (- coe_b) / 2 * coe_a
                    print(f"Unica solución: {x1}")

                else:
                    print("No existen soluciones reales para esta ecuación")

        case 4:
            print("Programa finalizado. Gracias por calcular con nosotros!")
            break 

        case _:
            print("El número ingresado no corresponde a ninguna operación")