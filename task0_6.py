def maximum(*args):
    max_number = args[0]
    for i in args:
        if i > max_number:
            max_number = i
    return max_number


print(maximum(10, 5, 31, 6))
