class OperacionAritmetica:
    def __init__(self):
        self.numero1 = None
        self.numero2 = None

    def ingresar_numeros(self):
        self.numero1 = int(input("Ingrese el primer número (entero): "))
        self.numero2 = int(input("Ingrese el segundo número (entero): "))

    def sumar(self):
        resultado = self.numero1 + self.numero2
        print("La suma es:", resultado)

    def restar(self):
        resultado = self.numero1 - self.numero2
        print("La resta es:", resultado)

    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        print("La multiplicación es:", resultado)

    def dividir(self):
        if self.numero1 == 0 and self.numero2 == 0:
            print("La división no se puede realizar: 0 entre 0 no está definida.")
        else:
            resultado = self.numero1 / self.numero2
            print("La división es:", resultado)

if __name__ == "__main__":
    operacion = OperacionAritmetica()
    while True:
        print("\nCalculadora:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            operacion.ingresar_numeros()
            operacion.sumar()
        elif opcion == "2":
            operacion.ingresar_numeros()
            operacion.restar()
        elif opcion == "3":
            operacion.ingresar_numeros()
            operacion.multiplicar()
        elif opcion == "4":
            operacion.ingresar_numeros()
            operacion.dividir()
        elif opcion == "5":
            print("Saliendo de la calculadora.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")