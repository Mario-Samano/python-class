secuencias = input("Ingrese las secuencias de ADN separadas por comas:\n").split(",")

secuencias_invertidas = [secuencia.strip()[::-1] for secuencia in secuencias]

print(f"Secuencias invertidas:\n {secuencias_invertidas}")