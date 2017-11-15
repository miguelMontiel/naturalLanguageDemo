import tkinter.filedialog as Tkinter
import os.path

inicio = "----------- STRING(S) FOUND -------------------"

archivo = Tkinter.askopenfile(title = "Archivos TXT")
archivoNew = 'C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia'
#NewfileChido = os.path.basename(archivo)

print(archivo)

for linea in archivo:
    if inicio in linea:
        tablaTitulo = linea[2:10]
        print(tablaTitulo)
        with open(archivoNew + archivo) as archivoNuevo:
            archivoNuevo.write("\n")
            archivoNuevo.write(tablaTitulo)

    for palabra in linea.split():
        if palabra == "FROM" or palabra == "MOVE" or palabra == "PIC":
            print(".")
            #blahhh.write(".")
archivo.close()
#blahhh.close()