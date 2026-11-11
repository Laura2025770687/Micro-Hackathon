import logica
import visual

largo_arreglo = int(input(f"Ingrese el largo del arreglo: "))
arr = largo_arreglo*[0]
for i in range(largo_arreglo):
    arr[i] = int(input(f"ingrese el num {i + 1}/{largo_arreglo} del arreglo: "))


arboles = [largo_arreglo]
aActivos = []

#                               logica
for arr, resaltar, tipo, msg in logica.smoothsort(arr, aActivos):
    # visual
    visual.estado(arr, resaltar, tipo, msg, aActivos, logica.posSerieLeon)
    # Pausa entre pasos 
    input("Presiona [ENTER] para el siguiente paso...")