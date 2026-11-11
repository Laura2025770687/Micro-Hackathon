"""
Smoothsort (algoritmo in-place, no usa memoria extra)

numero de Leonardo 
L(0) = 1, L(1) = 1, y para el resto, L(k) = L(k-1) + L(k-2) + 1

ej: 1, 1, 3, 5, etc.
"""
import visual


#intercambia dos elementos de un arreglo con las posiciones
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
    numSerieLeo, tamHijoDer = numLeon(arbolCop)

    while numSerieLeo > 1:
        iHijoDer = i -1
        iHijoIzq = i - tamHijoDer - 1
        yield list(arr), [i, iHijoDer, iHijoIzq], "COMPARA", f"Sift: comparando raíz {arr[i]} con sus hijos {arr[iHijoDer]} y {arr[iHijoIzq]}" 
        if arr[iHijoDer] > arr[iHijoIzq]:
            if arr[iHijoDer] > arr[i]:
                arr = intercambiar(arr, iHijoDer, i)
                yield list(arr), [i, iHijoDer], "INTERCAMBIA", f"Sift: intrcambio con el hijo mayor, {arr[iHijoDer]} y {arr[i]}" 
                i = iHijoDer
                arbolCop = tamHijoDer
                numSerieLeo, tamHijoDer = numLeon(arbolCop)
            else:
                break
        else:
            if arr[iHijoIzq] > arr[i]:
                arr = intercambiar(arr, iHijoIzq, i)
                yield list(arr), [i, iHijoIzq], "INTERCAMBIA", f"Sift: intrcambio con el hijo mayor, {arr[iHijoIzq]} y {arr[i]}" 
                i = iHijoIzq
                arbolCop = arbolCop - tamHijoDer - 1
                numSerieLeo, tamHijoDer = numLeon(arbolCop)
            else:
                break
    yield list(arr), [i], "OK_SIFT", f"Sift: terminó el sift" 

# para trinkle, das un numero positivo y te da esa iteracion del num de leon
def posSerieLeon(k):
    num_leon = [1,1]
    for i in range(k+1):
        proximo = num_leon[i] + num_leon[i+1] + 1
        num_leon.append(proximo)
    return num_leon[k]

# compara las raices (puntas) de los arboles y las intercambia
def trinkle (arreglo,aActivos,indice):
    # ultimo arbol activo
    socorro = len(aActivos) - 1

    while(socorro>0):
        # arbol de orden k actual
        k = aActivos[socorro]
        # indice del vecino = indice actual - arbol de orden k
        vecino = indice - posSerieLeon(k)

        yield list(arreglo), [indice, vecino], "COMPARA", f"Trinkle: comparando raíz actual {arreglo[indice]} (ind {indice}) con raíz vecina {arreglo[vecino]} (ind {vecino})"

        if(arreglo[vecino] <= arreglo[indice]):
            break
        if(k >= 2):
            # indice de los "hijos", uno es el indice anterior y el otro es el indice anterior menos el tamaño del arbol
            hijo_der = indice - 1
            hijo_comunista = indice - 1 - posSerieLeon(k-2)

            yield list(arreglo), [vecino, hijo_der, hijo_comunista], "COMPARA", f"Trinkle: validando si hijos ({arreglo[hijo_der]}, {arreglo[hijo_comunista]}) superan al vecino {arreglo[vecino]}"

            # Si los hijos son mayores no se puede hacer el cambio pq romperia la logica
            if arreglo[hijo_comunista] > arreglo[vecino] or arreglo[hijo_der] > arreglo[vecino]:
                break
        # si todo esta bn hacemos el cambio con switch
        arreglo[indice], arreglo[vecino] = arreglo[vecino], arreglo[indice]

        yield list(arreglo), [indice, vecino], "INTERCAMBIA", f"Trinkle: cambio entre raíces {arreglo[indice]} y {arreglo[vecino]}"

        indice = vecino
        socorro -= 1

    if aActivos[socorro] >= 2:
        yield from sift(arreglo, indice, posSerieLeon(aActivos[socorro]))

# actualiza los arboles cuando dos se fucionan o cuando se agregan +
def actualizarArboles(aActivos):
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
    return aActivos

# funcion principal de ordenamiento
def smoothsort(arr, aActivos):
    n = len(arr)

    # paso 1 formar arbol, recorriendo el arreglo de principio a final
    for i in range(len(arr)):
        actualizarArboles(aActivos)

        yield list(arr), [i], "NUEVO_NODO", f"Fase 1: Elemento {arr[i]} (ind {i}) ingresa al bosque. Órdenes: {aActivos}"

        yield from trinkle(arr, aActivos, i)

    # paso 2 ir eliminando los arboles del final del arreglo (menos el ultimo que ya esta odenado)
    # hasta el principio
    for i in range(n-1, 0, -1):
        k = aActivos.pop()

        if k == 0 or k == 1:
            # los arboles de tamaño 1 no tienen hijos asi que la raíz queda fija
            yield list(arr), [i], "FIJADO", f"Fase 2: Elemento {arr[i]} (ind {i}) fijado en su posición final"
        else:

            # arbol de orden k >= 2 al fijar la raiz se divide en sus dos hijos
            # Hijo izquierdo (orden k-1) 
            # e Hijo derecho (orden k-2)
            k_izq = k - 1
            k_der = k - 2
            
            # indices de las raices de esos dos nuevos arboles en el arreglo
            idx_der = i - 1
            idx_izq = i - 1 - posSerieLeon(k_der)

            # 1 el hijo izquierdo y derecho se incorporan al bosque
            aActivos.append(k_izq)
            aActivos.append(k_der)

            # se fija
            yield list(arr), [i], "FIJADO", f"Fase 2: Elemento {arr[i]} fijado. Árbol L({k}) desmantelado en L({k-1}) y L({k-2})"

            # se revisan las raices de los arboles que quedan al desacer el anterior
            yield from trinkle(arr, aActivos, idx_der)
       
    # El elemento en el índice 0 queda fijado por descarte
    yield list(arr), [0], "FINALIZADO", "Fase 2: Arreglo completamente ordenado"
        