inputfile = "dna_sequences.txt" 
outputfile = "dna_sequences.fa" 

#------------------------------------------------------------------- leemos el archivo
with open (inputfile, "r") as infile, open(outputfile, "w") as outfile:
    for linea in infile: 
        id, seq = linea.strip().split("\t")

        # ---------------------------------- mandar a un archivo de salida formato fasta 
        outputfile.write(f">{id}\n{seq.upper()}\n")
    