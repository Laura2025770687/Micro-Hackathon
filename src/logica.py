"""
Smoothsort (algoritmo in-place, no usa memoria extra)

numero de Leonardo 
L(0) = 1, L(1) = 1, y para el resto, L(k) = L(k-1) + L(k-2) + 1

ej: 1, 1, 3, 5, etc.
"""

def intercambiar(arr, pos1, pos2):
    aux = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = aux
    return arr

# se le entrega un numero de la serie leo y le devuelve la posicion en 
# la serie y el num anterior (ej: 9 de la serie, devuelve 4 (1, 3, 5, 9) de pos y 5 de anterior)
def numLeon(num):
    if num == 1:
        return 1, 0
    else:
        nMenos2 = 1
        nMenos1 = 1
        n = 3
        cont = 2
        while n <= num:
            if n == num:
                return cont, nMenos2
            nMenos2 = nMenos1
            nMenos1 = n
            n = nMenos2 + nMenos1 + 1
            cont += 1

# recibe arreglo, posicion i en el arreglo (raiz del arbol) y 
# arbol (cantidad de elementos del arbol (coincide con un numero leo) )
def sift(arr, i, arbol):
    arbolCop = arbol
    numSerieLeo = 2

    while numSerieLeo > 1:
        print("Arreglo: ", arr, "\n")
        numSerieLeo, tamHijoDer = numLeon(arbolCop)
        iHijoDer = i -1
        iHijoIzq = i - tamHijoDer - 1
        if arr[iHijoDer] > arr[iHijoIzq]:
            if arr[iHijoDer] > arr[i]:
                arr = intercambiar(arr, iHijoDer, i)
                i = iHijoDer
                arbolCop = tamHijoDer
            else:
                break
        else:
            if arr[iHijoIzq] > arr[i]:
                arr = intercambiar(arr, iHijoIzq, i)
                i = iHijoIzq
                arbolCop = arbolCop - tamHijoDer - 1
            else:
                break


arr = 5*[0]

for i in range(5):
    arr[i] = int(input(f"ingrese el num {i + 1}/5 del arreglo: "))


arboles = [5]

# 4 de el ultimo elemento en la lista arr
sift(arr, 4, arboles[0])
    
print( arr, "\n")






