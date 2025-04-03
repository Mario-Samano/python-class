inputfile = "4_input_adapters.txt"
outputfile = "4_input_no_adapters.txt"

with open(inputfile, "r") as infile, open(outputfile, "w") as outfile:  # Modo "w" para escritura
    for linea in infile:
        # Cortar los adaptadores 
        secuencia_limpia = linea.strip()[14:]
        # Escribir en el archivo de salida 
        outfile.write(f"{secuencia_limpia}\n")  
