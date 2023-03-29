# Ingresar un numero y si este es entero multiplicarlo consigo mismo e imprimir el resultado

num = int(input("Ingrese el numero: "))

if num % 2 == 0:
    resultado = num * num
    print(f"El resultado de al multlicar los enteros es: {resultado}")
else:
    print("No se hace la operacion ya que el numero que ingresate no es entero")




