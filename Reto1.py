# Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

numero = int(input("Digite el numero: "))

while numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"El numero es {numero} FizzBuzz")
    elif numero % 3 == 0:
        print(f"El numero {numero} Fizz")
    elif numero % 5 == 0:                                     #Usando el ciclo while#
        print(f"El numero {numero} Buzz")
    else:
        print(f"El numero {numero} no es divisble")
    numero = int(input())

print(" ")

n = int(input("Diguite el numero: "))

for n in range(1,100):
    if n % 3 == 0 and n % 5 == 0:
        print(f"El numero {n} es FizzBuzz")
    elif n % 3 == 0:                                    #Usando el ciclo for#
        print(f"El numero {n} es Fizz")
    elif n % 5 == 0:
        print(f"El numero {n} es Buzz")
    else:
        print(f"El numero {n} no es divisible ni por 5 ni 3")

# Escribe un programa por consola que me muestre si el numero es par o imapr usando el ciclo while

num = int(input("Digite el número--: "))

while num != 0:
    if num % 2 == 0:
        print(f"El número {num} es par")
    elif num == 0:
        break
    else:
        print(f"El número {num} es impar")
    num = int(input("Diguite un nuevo numero: "))


