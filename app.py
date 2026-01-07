from operaciones import OperacionAritmetica

if __name__ == "__main__":
    # Ejecutar la calculadora interactiva definida en operaciones.py
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