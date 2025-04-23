def count_alpha_digits(string):
    alpha = 0
    digits = 0
    for char in string:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            digits += 1
    return {'alpha': alpha, 'digits': digits}

string = "Example string 421312"
result = count_alpha_digits(string)
print(result)
