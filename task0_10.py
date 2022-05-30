def common_letters(string1, string2):
    string1_lower = string1.lower()
    string2_lower = string2.lower()

    common_letters_list = []
    for item in string1_lower:
        if item in string2_lower:
            common_letters_list.append(item)
            no_duplicates = []
            for i in common_letters_list:
                if i not in no_duplicates:
                    no_duplicates.append(i)
            join_common_letters = ", ".join(no_duplicates)

    print("common letters found: ", join_common_letters)


common_letters("house", "computers")
