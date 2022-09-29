def power(lista):
    power = []
    for i in lista:
        power.append(i**2)
    return power

print(power([1, 3, 6]))

def power2(lista, wykladnik):
    power2 = []
    for i in lista:
        power2.append(i**wykladnik)
    return power2

print(power2([1, 3, 6], 3))