numero_str = input("dame 3 numeros separados por un espacio:   ").split()
print(numero_str)
print(list(map(int,numero_str))) # ----------------------------------------- No es necesario hacer un lista ya que map hace un objeto iterable 
lista_numeros = list(map(int,numero_str))

suma = sum(lista_numeros)
print(suma)

#num = [1, 2, 3]
#suma_numeros = sum(num)
#print(suma_numeros)