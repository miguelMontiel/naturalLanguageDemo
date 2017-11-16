import tkinter.filedialog as Tkinter
import os.path

inicio = "----------- STRING(S) FOUND -------------------"

archivo = Tkinter.askopenfilename(initialdir="C:/Users/mainUser/PycharmProjects/naturalLanguageDemo", title="Archivos TXT")
archivoNuevo = "C:/Users/mainUser/Desktop/laYessenia/" + "Chido-" + os.path.basename(str(archivo))

archivos = open(archivo, "r")
archivoNuevos = open(archivoNuevo, "w+")

for linea in archivos:
    if inicio in linea:
        tablaTitulo = linea[2:10]
        print(tablaTitulo)
        archivoNuevos.write("\n")
        archivoNuevos.write(tablaTitulo + " ")

    for palabra in linea.split():
        if palabra == "FROM" or palabra == "MOVE" or palabra == "PIC":
            archivoNuevos.write(".")
archivos.close()
archivoNuevos.close()