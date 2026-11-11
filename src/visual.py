import os
import time

# para la funcion d ebosque, imprime los numeros del arreglo
def imprimir_nodo(arr, resaltar, tipo , i, k, posSerieLeon, prefijo="", es_ultimo=True):
    conector = "└── " if es_ultimo else "├── "

    #se imprimen los valores del arreglo
    if i in resaltar:
            color = "\033[92m" if tipo == "INTERCAMBIA" else "\033[93m"
            print(f"{prefijo}{conector}{color}{arr[i]}\033[0m (ind {i})")
    else:
            print(f"{prefijo}{conector}{arr[i]} (ind {i})")
    
    
    if k <= 1:
        return
        
    idx_der = i - 1
    idx_izq = i - 1 - posSerieLeon(k - 2)
    
    # de forma recursiva se imprimen los demas ¿
    nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
    imprimir_nodo(arr, resaltar, tipo, idx_izq, k - 1, posSerieLeon, nuevo_prefijo, False)
    imprimir_nodo(arr, resaltar, tipo, idx_der, k - 2, posSerieLeon, nuevo_prefijo, True)

# imorime como arbol los numeros del arreglo
def dibujar_bosque(arr, resaltar, tipo, aActivos, posSerieLeon):
    print("\n --- BOSQUE DE LEONARDO :) ")
    if not aActivos:
        print("(Bosque vacío)")
        return

    # calcula los indices donde cae la raiz de cada árbol activo
    # la suma de tamaños de los arboles anteriores nos da donde termina cada uno
    raices = []
    ind_acumulado = -1
    for k in aActivos:
        ind_acumulado += posSerieLeon(k)
        raices.append(ind_acumulado)

    # dibuja cada arbol del bosque
    for num_arbol, (k, raiz_ind) in enumerate(zip(aActivos, raices), 1):
        tam = posSerieLeon(k)
        print(f"\nÁrbol: ")
        imprimir_nodo(arr, resaltar, tipo, raiz_ind, k, posSerieLeon, prefijo="", es_ultimo=True)
    print("\n")


# funcion principal de la parte visual, usa todas laas demas
def estado(arr, resaltar, tipo, msg, aActivos, posSerieLeon):
    
    # se limpia la termial en cada vez
    os.system("clear" if os.name == "posix" else "cls")

    print("\n ----- SMOOTHSORT -----")

    print(f"\nACCION: [{tipo}] {msg}\n")

    # fila de los indices del arreglo
    arr_indices = "Indice: "
    for ind in range(len(arr)):
        arr_indices += f"[{ind}] "
    print(arr_indices)

    # fila de los elementos del arreglo
    arr_valores = "Valor : "
    for ind in range(len(arr)):
        # si estan en resaltar los marca de otro color
        if ind in resaltar:
            color = "\033[92m" if tipo == "INTERCAMBIA" else "\033[93m"
            arr_valores += f"{color}[{arr[ind]}]\033[0m "
        else:
            arr_valores += f"[{arr[ind]}] "
    print(arr_valores)

    print("\n")

    # imprime el bosque en pantalla
    dibujar_bosque(arr, resaltar, tipo, aActivos, posSerieLeon)
