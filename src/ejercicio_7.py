secuencias = input("Dame las secuencias, por favor separalas por comas: \n").split(",")

codones_de_inicio = [secuencia.strip() [:3] for secuencia in secuencias]
print (f"Los codones son: {codones_de_inicio}")