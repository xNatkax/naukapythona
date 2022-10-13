def remove_odd(word):
    new_word = []
    letters = list(word)
    for i in letters[::2]:
        if i != letters:
            new_word.append(i)
            
    return new_word


x = remove_odd("Dawid")

print(x)