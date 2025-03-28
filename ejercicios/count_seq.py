inputfile = "secuencias.fa"
with open(inputfile, "r") as infile:
    lineas = infile.readlines()
print (lineas[0])
print (lineas[1])
[linea for linea in lineas if linea.startswith(">")]