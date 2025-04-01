from datetime import datetime


def get_days_from_today(date: str) -> str | int:
    try:
        # Перетворення рядка дати у об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Отримання поточної дати
        today = datetime.today().date()

        # Різниця між поточною датою та заданою датою
        delta = today - given_date

        # Повертаємо різницю у днях
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."