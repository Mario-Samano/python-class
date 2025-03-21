numero_str = input("dame 3 numeros separados por un espacio:   ").split()
print(numero_str)
print(list(map(int,numero_str)))
lista_numeros = list(map(int,numero_str))

suma = sum(lista_numeros)
print(lista_numeros)

#num = [1, 2, 3]
#suma_numeros = sum(num)
#print(suma_numeros)