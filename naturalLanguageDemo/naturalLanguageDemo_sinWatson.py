import tkinter.filedialog as Tkinter
import os.path

inicio = "----------- STRING(S) FOUND -------------------"

archivo = Tkinter.askopenfilename(initialdir="C:/Users/mainUser/PycharmProjects/naturalLanguageDemo", title="Archivos TXT")
temp = "C:/Users/mainUser/Desktop/laYessenia/" + "temp.txt"

archivos = open(archivo, "r")
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


archivoNuevo2 = "C:/Users/mainUser/Desktop/laYessenia/" + "Chido-" + os.path.basename(str(archivo))

archivos2 = open("C:/Users/mainUser/Desktop/laYessenia/temp.txt", "r")
archivoFinal = open(archivoNuevo2, "w+")

for linea2 in archivos2:
    if "." in linea2:
        ayuda = linea2.replace(".", "")
        print("Si tiene: ", ayuda)
        archivoFinal.write(ayuda)
    else:
        print("No tiene: ", linea2)

archivos2.close()
archivoFinal.close()
