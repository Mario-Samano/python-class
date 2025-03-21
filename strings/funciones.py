secuencia = "GTACGATCA"
for i, base in enumerate(secuencia): 
    print(f"posicion: {i} : {base}")

"""
Funcion zip: itera sobre varias listas ----> xd 
"""

bases = "ATGC"
complementos = "TACG"

for base, complemento in zip (bases, complementos):
    print(f"la base es {base} y su complemento es {complemento}")