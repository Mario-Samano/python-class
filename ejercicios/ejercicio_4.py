inputfile = "4_input_adapters.txt"
outputfile = "4_input_no_adapters.txt"

with open (inputfile, "r") as infile, open(outputfile) as outfile:
    for linea in infile:
        #----------------------------------- cortar los adaptadores 
        secuencia_limpia = linea.strip()[14:]
        # ---------------------------------- mandar a un archivo de salida 
        outfile.write(f"{secuencia_limpia}\n")
