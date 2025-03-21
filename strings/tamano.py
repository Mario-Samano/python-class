with open("genes.gff") as file:
    for linea in file: 
        # quitar los saltos de linea
        columna = linea.strip().split("\t")
        tamano = int(columna[4]) - int(columna[3])
        print(tamano)