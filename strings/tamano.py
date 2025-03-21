with open("genes.gff") as file:
    for linea in file: 
        # quitar los saltos de linea
        columna = linea.split().strip("\t")
        print(columna[3])