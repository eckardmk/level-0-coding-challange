def two_strings(string1, string2):
    common = list()
    for i in string1:
        if i in string2 and i not in common:
            common.append(i)
    return common


print(two_strings("house", "computers"))
