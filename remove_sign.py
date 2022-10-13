def remove_sign(word, n):
    new_word = ""
    
    for i in word:
        if i != n:
            new_word += i
    return new_word

x = remove_sign("abcedako", "a")

print(x)