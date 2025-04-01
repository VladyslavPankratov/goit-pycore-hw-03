import random


def get_numbers_ticket(min, max, quantity):
    # Перевірка правильності вхідних параметрів
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортування та повернення результату
    return sorted(numbers)


# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)
