archivo = open("archivo.txt")
archivoNuevo = open("archivoNuevo.txt", "w")

for linea in archivo:
    if '-------' in linea:
        print(linea)
        archivoNuevo.write("\n")
        archivoNuevo.write(linea)

    for palabra in linea.split():
        if palabra == "INCLUDE":
            print(linea)
            archivoNuevo.write(linea)

        if palabra == "FROM":
            print(linea)
            archivoNuevo.write(linea)

        if palabra == "MOVE":
            print(linea)
            archivoNuevo.write(linea)

archivo.close()
archivoNuevo.close()