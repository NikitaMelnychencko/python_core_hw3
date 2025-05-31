import random

# min - мінімальне можливе число у наборі (не менше 1).
# max - максимальне можливе число у наборі (не більше 1000).
# quantity - кількість чисел, які потрібно вибрати (значення між min і max).

def get_numbers_ticket(min:int, max:int, quantity:int)->list[int]:
    numbers = []

    if min < 1 or max > 1000 or quantity < 1:
        return "Invalid input"

    while len(numbers) < quantity:
        number = random.randint(min, max)
        if number not in numbers:
            numbers.append(number)
    return numbers


def get_parametrs(type:str)->int:
    return input(f"Enter the {type}: ")

def validation_input(value:str, type:str)->int:
    if not value:
        print(f"No {type} provided")
        value = get_parametrs(type)
        return validation_input(value, type)
    elif not value.isdigit():
        print(f"Invalid {type}")
        value = get_parametrs(type)
        return validation_input(value, type)
    else:
        return int(value)

min = validation_input(get_parametrs("minimum number"), "minimum number")
max = validation_input(get_parametrs("maximum number"), "maximum number")
quantity = validation_input(get_parametrs("quantity of numbers"), "quantity of numbers")

lottery_numbers = get_numbers_ticket(min, max, quantity)
print(lottery_numbers)