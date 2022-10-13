def remove_odd_2(word):
    word_list = list(word)
    new_word = ''.join(word_list[::2])
    return new_word

x = remove_odd_2("Dawid")

print(x)


