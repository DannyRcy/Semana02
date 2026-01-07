from operaciones import OperacionAritmetica
if __name__ == "__main__":
    operacion = OperacionAritmetica()
    operacion.sumar()
    def __init__(self):
        self.numero1 = int(input("Ingrese el primer número (entero): "))
        self.numero2 = int(input("Ingrese el segundo número (entero): "))
    def sumar(self):
        resultado = self.numero1 + self.numero2
        print("La suma es:", resultado)


