secuencias = input("Ingrese las secuencias de ADN separadas por comas:\n").split(",")

# -----------------------------------------------------------------Invertir cada secuencia
secuencias_invertidas = [secuencia.strip()[::-1] for secuencia in secuencias]

# Imprimir las secuencias invertidas
print(f"Secuencias invertidas:\n {secuencias_invertidas}")