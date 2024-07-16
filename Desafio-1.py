def invertir_y_filtrar(arr, S):
    arr_fil = []
    for num in arr:
        nuevo_num = ''.join([d for d in str(num) if int(d) < S])
        if nuevo_num != '':
            arr_fil.append(int(nuevo_num))
    
    return arr_fil[::-1] 

print(invertir_y_filtrar([1, 2, 3, 4, 5, 6], 3))
print(invertir_y_filtrar([10, 20, 30, 40], 3))
print(invertir_y_filtrar([6], 3))
