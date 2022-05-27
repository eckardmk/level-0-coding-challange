def vowel_check(string):
    new_string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    present_vowels = []
    for item in new_string:
        if item in vowels:
            present_vowels.append(item)
            non_duplicates = []
            for i in present_vowels:
                if i not in non_duplicates:
                    non_duplicates.append(i)
            join_present_vowels = ", ".join(non_duplicates)
    print("vowels: ", join_present_vowels)


vowel_check("Umuzi")
