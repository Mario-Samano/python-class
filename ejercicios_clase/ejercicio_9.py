secuencias = input("Dame las secuencias:\n").split(",") # guarda las secuencias
lista_de_RNA = [secuencia.replace("T", "U") for secuencia in secuencias]
print (f"Las secuencias de RNA son:\n {lista_de_RNA}")
