import re


def normalize_phone(phone_number):
    # Видаляємо всі непотрібні символи, включаючи знак '+', якщо він знаходиться між цифрами
    cleaned_number = re.sub(r'[^0-9]', '', phone_number)  # Видаляємо все, що не є цифрами

    # Перевіряємо, чи номер вже містить міжнародний код (починається з '380')
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    elif cleaned_number.startswith('0'):
        # Якщо номер починається з '0', додаємо міжнародний код '+38'
        return '+38' + cleaned_number[1:]
    else:
        # Якщо номер не містить жодного коду, додаємо міжнародний код '+38'
        return '+38' + cleaned_number


# Приклад використання
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
    "+38+0501234567",  # Додав приклад, де '+' між цифрами
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

