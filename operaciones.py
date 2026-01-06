while True:
    try:
        numero1 = int(input("Ingrese el primer número (entero): "))
        numero2 = int(input("Ingrese el segundo número (entero): "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

suma = numero1 + numero2
print("La suma es:", suma)