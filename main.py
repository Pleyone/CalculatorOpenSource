import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = sumar.sumar(a, b)
            print("El resultado es:", resultado)
        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = resta.restar(a, b)
            print("El resultado es:", resultado)
        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion.multiplicar(a, b)
            print("El resultado es:", resultado)
        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = dividir.dividir(a, b)
            print("El resultado es:", resultado)
        elif opcion == "5":
            cantidad_numeros = int(input("Ingrese la cantidad de números a sumar: "))
            numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(cantidad_numeros)]
            resultado = suma_avanzada.suma_avanzada(*numeros)
            print("El resultado es:", resultado)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
