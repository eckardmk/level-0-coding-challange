def maximum(*args):
    maximum_number = args[0]
    for item in args:
        if item > maximum_number:
            maximum_number = item
    return maximum_number


print(maximum(10, 5, 31, 6))
