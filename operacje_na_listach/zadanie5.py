def replace(ciag, str1, str2):
    nowy_ciag = ''
    for i in ciag:
        if i == str1:
            nowy_ciag += str2
        else:
            nowy_ciag += i
    return nowy_ciag

print(replace('dawidkosiak', 'i', 'k'))




