def is_dict_empty(d):
    return not bool(d)

# Example usage
my_dict = {}
print(is_dict_empty(my_dict))  # Output: True

my_dict = {"key": "value"}
print(is_dict_empty(my_dict))  # Output: False