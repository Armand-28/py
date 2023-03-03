# Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)



numero = int(input("Introduce el numero: "))

while numero != 0:
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    numero = int(input("Introduce otro numero o oprime 0 para salir: "))


while True:
    print("Operaciones disponibles: ")
    print(" ")
    print("[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicación")
    print("[4] Division")
    print("[5] Salir")
    opcion = 0

    opcion = int(input("Seleccone la operacion que desea realizar: "))

    if opcion == 5:
        break

    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el Segundo numero: "))

    if opcion == 1:
        resultado = numero1 + numero2
        print("El resultado de la suma es: ",resultado)
        elif opcion == 2:
            resultado = numero1 + numero2
            print("El resultado de la resta es: ",resultado)
        elif opcion == 3:
            resultado = numero1 * numero2
            print("El resulatdo de la multiplicacion es: ",resultado)
        elif opcion == 4:
            resultado = numero1 / numero2
            print("El resultado de la division es: ",resultado)
        else:
            print("Opcion invalida (error)")
            print(" ")
if opcion == 0:
    opcion = opcion+1
if opcion != 0:
    print("Desea seguir con las operaciones")
    print(" ")
    print("[0] Si")
    print("[5] No")
    opcion = int(input())
    

