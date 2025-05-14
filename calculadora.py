def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def calculadora():
    print("Operaciones disponibles:")
    print("1. Restar")
    print("2. Sumar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1/2/3/4): ")

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: por favor, ingresa números válidos.")
        return

    if opcion == '2':
        print("Resultado:", sumar(num1, num2))
    elif opcion == '1':
        print("Resultado:", restar(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
        print("Resultado:", dividir(num1, num2))
    else:
        print("Error grave")

# Ejecutar la calculadora
calculadora()
