secuencias = input("Ingrese las secuencias, recuerde separarlas por comas: \n").split(",")

contadores = [print(f"A: {secuencia.count("A")}"), secuencia.count("G"), secuencia.count("C"), secuencia.count("T")] for secuencia in secuencias]
# --------------- conteo de cada uno 
print(contadores)

