lista = [1, 3, 7, 11, 2, -6, 0]
najmniejsza = None
najwieksza = None
for i in lista:
    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i
    if najwieksza == None or najwieksza < i:
        najwieksza = i
print("najmniejsza: ", najmniejsza)
print("najwieksza: ", najwieksza)