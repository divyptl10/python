def get_integer_input():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

integer_value = get_integer_input()
print(f"You entered the integer: {integer_value}")
