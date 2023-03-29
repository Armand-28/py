# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
#  Un Anagrama consiste en formar una palabra reordenando TODAS
#  las letras de otra palabra inicial.
#  NO hace falta comprobar que ambas palabras existan.
#  Dos palabras exactamente iguales no son anagrama.

def anagrama(cad1,cad2):
    return sorted(cad1) == sorted(cad2)

print(anagrama("amor","ramo"))

def anagrama2(str1,str2):
    return sorted(str1) == sorted(str2)
print(anagrama2("mocasin","caminos"))