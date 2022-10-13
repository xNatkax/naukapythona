def take(lista, liczba_elementów):
    nowa_lista = []
    for i in lista:
        if len(nowa_lista) == liczba_elementów:
            return nowa_lista
        else:
            nowa_lista.append(i)
    return nowa_lista

print(take([1, 4, 6, 8], 2))
