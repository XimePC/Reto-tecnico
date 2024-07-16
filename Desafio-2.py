def cuadrados_ordenados_filtrados(arreglo, S):
    SS = S * 10 + S  

    arreglo_filtrado = [x**2 for x in arreglo if 0 <= x**2 <= SS]
    

    n = len(arreglo_filtrado)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo_filtrado[j] > arreglo_filtrado[j+1]:
                arreglo_filtrado[j], arreglo_filtrado[j+1] = arreglo_filtrado[j+1], arreglo_filtrado[j]
    
    return arreglo_filtrado

print(cuadrados_ordenados_filtrados([1, 2, 3, 5, 6, 8, 9], 3))
print(cuadrados_ordenados_filtrados([-2, -1], 3))
print(cuadrados_ordenados_filtrados([-6, -5, 0, 5, 6], 3))
