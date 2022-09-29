def reject(lista):
    parzyste = []
    for i in lista:
        if i % 2 == 0:
            parzyste.append(i)
    return parzyste

print(reject([1, 2, 4, 6, 7, 9, 10, 13, 16, 27, 29, 30]))
