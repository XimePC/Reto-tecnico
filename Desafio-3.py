def cambio_minimo(monedas):

    n = len(monedas)
    for i in range(n):
        for j in range(0, n-i-1):
            if monedas[j] > monedas[j+1]:
                monedas[j], monedas[j+1] = monedas[j+1], monedas[j]

    cambio_actual_creado = 0
    for moneda in monedas:
        if moneda > cambio_actual_creado + 1:
            return cambio_actual_creado + 1
        cambio_actual_creado += moneda
    return cambio_actual_creado + 1

print(cambio_minimo([5, 7, 1, 1, 2, 3, 22]))
print(cambio_minimo([1, 1, 1, 1, 1]))        
print(cambio_minimo([1, 5, 1, 1, 1, 10, 15, 20, 100])) 
