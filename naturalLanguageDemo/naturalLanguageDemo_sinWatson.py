import tkinter.filedialog as Tkinter
import os.path

inicio = "----------- STRING(S) FOUND -------------------"

archivo = Tkinter.askopenfilenames(initialdir="C:/Users/IBM_ADMIN/Desktop/archivosOriginales/", title="Archivos TXT")
temp = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/temp.txt"

for individuales in archivo:
    archivos = open(individuales, "r")
    archivoNuevo = open(temp, "w+")

    for linea in archivos:
        if inicio in linea:
            tablaTitulo = linea[2:10]
            archivoNuevo.write("\n")
            archivoNuevo.write(tablaTitulo + " ")

        for palabra in linea.split():
            if palabra == "FROM" or palabra == "MOVE" or palabra == "PIC":
                archivoNuevo.write(".")

    archivos.close()
    archivoNuevo.close()


    archivoNuevo2 = "C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/" + "Chido-" + os.path.basename(str(individuales))

    archivos2 = open("C:/Users/IBM_ADMIN/Desktop/archivosLaYessenia/temp.txt", "r")
    archivoFinal = open(archivoNuevo2, "w+")

    for linea2 in archivos2:
        if "." in linea2:
            ayuda = linea2.replace(".", "")
            archivoFinal.write(ayuda)

    print(individuales)
    archivos2.close()
    archivoFinal.close()