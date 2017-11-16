import tkinter.filedialog as Tkinter
import os.path

inicio = "----------- STRING(S) FOUND -------------------"

archivo = Tkinter.askopenfile(initialdir="C:/Users/mainUser/PycharmProjects/naturalLanguageDemo", title="Archivos TXT")

if archivo is None:
    print("No seleccionaste archivo")

#archivoNew = 'C:/Users/mainUser/Desktop/archivosLaYessenia/'
archivoNuevo = open("archivoNuevo.txt", "w")

print(archivo)

for linea in archivo:
    if inicio in linea:
        tablaTitulo = linea[2:10]
        print(tablaTitulo)
        archivoNuevo.write("\n")
        archivoNuevo.write(tablaTitulo)

    for palabra in linea.split():
        if palabra == "FROM" or palabra == "MOVE" or palabra == "PIC":
            print(".")
            archivoNuevo.write(".")

archivo.close()
archivoNuevo.close()
