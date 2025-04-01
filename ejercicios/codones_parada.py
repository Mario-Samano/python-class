secuencias = input("Ingrese las secuencias: \n").split(",")
#------------------------------------------------------------------------------------------------------------------------------ Filtrado de las cadenas
codones_de_parada =  [secuencia  for secuencia in secuencias if "TAA" in secuencia or "TAG" in secuencia or "TGA" in secuencia]
print(f"Las secuencias con codones de paro son: {codones_de_parada}")

