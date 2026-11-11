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



# 30 numeros leonardos pq pa que más
num_leon = [1,1]
for i in range(30):
    proximo = num_leon[i] + num_leon[i+1] + 1
    num_leon.append(proximo)


def trinkle (arreglo,aActivos,num_leon,indice):
    # ultimo arbol activo
    socorro = len(aActivos) - 1

    while(socorro>0):
        # arbol de orden k actual
        k = aActivos[socorro]
        # indice del vecino = indice actual - arbol de orden k
        vecino = indice - num_leon[k]
        if(arreglo[vecino] <= arreglo[indice]):
            break
        if(k >= 2):
            # indice de los "hijos", uno es el indice anterior y el otro es el indice anterior menos el tamaño del arbol
            hijo_der = indice - 1
            hijo_comunista = indice - 1 - num_leon[k-2]
            # Si los hijos son mayores no se puede hacer el cambio pq romperia la logica
            if arreglo[hijo_comunista] > arreglo[vecino] or arreglo[hijo_der] > arreglo[vecino]:
                break
        # si todo esta bn hacemos el cambio con switch
        arreglo[indice], arreglo[vecino] = arreglo[vecino], arreglo[indice]

        indice = vecino
        socorro -= 1
    sift(arreglo, indice, num_leon[aActivos[socorro]])

largo_arreglo = int(input(f"Ingrese el largo del arreglo: "))
arr = largo_arreglo*[0]
for i in range(largo_arreglo):
    arr[i] = int(input(f"ingrese el num {i + 1}/{largo_arreglo} del arreglo: "))


arboles = [largo_arreglo]

aActivos = []

for i in range(len(arr)):
    # Si hay 2 arboles y son de numeros leonardos consecutivos se juntan
    if len(aActivos) >= 2 and aActivos[-2] == aActivos[-1] + 1:
        # sacamos los 2 arboles
        aActivos.pop()
        k_mayor = aActivos.pop()

        # ponemos el nuevo arbol
        aActivos.append(k_mayor + 1)
        
    # si no, se crea otro aparte
    else:
        if len(aActivos) > 0 and aActivos[-1] == 1:
            aActivos.append(0)
        else:
            aActivos.append(1)
    trinkle(arr, aActivos, num_leon, i)
    
print( arr, "\n")