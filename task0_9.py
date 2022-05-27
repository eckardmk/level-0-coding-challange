def vowels(word):
    for letter in word.lower():
        if letter in "aeiou":
            print(letter)

    x = list()
    for letter in word.lower():
        if letter in "aeiou" and letter not in x:
            x.append(letter)


vowels("Umuzi")
