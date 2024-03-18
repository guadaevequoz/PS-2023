# modulo de la calculadora

from src import operations


def calculate():
    print("--- CALCULADORA (Grupo 14) ---")
    num1 = float(input("Ingresa un número: "))
    num2 = float(input("Ingresa otro número: "))

    print("Suma: ", operations.add(num1, num2))
    print("Resta: ", operations.substract(num1, num2))
    print("Multiplicar: ", operations.multiply(num1, num2))
    print("Dividir: ", operations.divide(num1, num2))