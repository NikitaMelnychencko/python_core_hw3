import re

def normalize_phone(phone_number:str)->str:
    if phone_number is None:
        print("Phone number is None")
        return ""

    if len(phone_number) < 10:
        print(f"Phone number {phone_number} is too short")
        return ""

    pattern = r"\d+"
    matches = re.findall(pattern, phone_number)
    value = "".join(matches)

    if not value:
        print("Empty phone number")
        return ""

    if (len(value) == 10):
        return f"+38{value}"
    elif (len(value) == 11 and value.startswith("3")):
        return f"+{value}"
    elif (value.startswith("38") and len(value) == 12):
        return f"+{value}"
    else:
        print(f"Invalid phone number format: {phone_number}")
        return ""


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "385-555-55-55",
    "5555",
    None,
    "jjdflgjfdkjfd"

]

sanitized_numbers = []
for num in raw_numbers:
  value =  normalize_phone(num)
  if value:
    sanitized_numbers.append(value)

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
