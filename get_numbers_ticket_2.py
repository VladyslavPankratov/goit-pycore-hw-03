import random


def get_numbers_ticket(min, max, quantity):
    print("Перевірка параметрів...")  # Додано для перевірки
    # Перевірка правильності вхідних параметрів
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []

    print("Параметри правильні, генеруємо числа...")  # Додано для перевірки
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортування та повернення результату
    return sorted(numbers)


def generate_ticket():
    print("Запуск програми генерації лотерейних квитків...")  # Додано для перевірки
    while True:
        try:
            # Отримуємо вхідні параметри від користувача
            min_value = int(input("Введіть мінімальне значення (1-1000): "))
            max_value = int(input("Введіть максимальне значення (1-1000): "))
            quantity = int(input(f"Введіть кількість чисел (між {min_value} і {max_value}): "))

            # Генерація лотерейного квитка
            lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)

            if lottery_numbers:
                print("Ваші лотерейні числа:", lottery_numbers)
            else:
                print("Невірні параметри. Спробуйте знову.")

            # Запит на продовження або завершення
            continue_choice = input("Бажаєте згенерувати новий квиток? (так/ні): ").strip().lower()
            if continue_choice != "так":
                print("Дякую за використання програми!")
                break
        except ValueError:
            print("Будь ласка, вводьте лише числа.")


generate_ticket()
