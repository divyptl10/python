
def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

input_string = input("Enter a string: ")
frequency= char_frequency(input_string)
print("Character frequency:", frequency)
