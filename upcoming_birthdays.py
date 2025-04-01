from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    # Отримуємо поточну дату
    today = datetime.today().date()

    upcoming_birthdays = []

    # Проходимо по кожному користувачу в списку
    for user in users:
        # Перетворюємо дату народження на об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Перевіряємо, чи вже минув день народження в цьому році
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            # Якщо минув, переводимо на наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Якщо день народження в наступні 7 днів
        if today <= birthday_this_year <= today + timedelta(days=7):
            # Перевіряємо, чи день народження припадає на вихідний
            if birthday_this_year.weekday() == 5:  # Субота
                # Переносимо на понеділок (додаємо 2 дні)
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя
                # Переносимо на понеділок (додаємо 1 день)
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                # Якщо день народження припадає на робочий день
                congratulation_date = birthday_this_year

            # Додаємо користувача з датою привітання в список
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


# Приклад використання функції
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1982.02.15"},
    {"name": "Bob Brown", "birthday": "1991.03.10"},
    {"name": "Charlie Davis", "birthday": "1987.04.05"},
    {"name": "David Miller", "birthday": "1983.05.12"},
    {"name": "Emily Wilson", "birthday": "1995.06.25"},
    {"name": "Frank Moore", "birthday": "1988.07.03"},
    {"name": "Grace Lee", "birthday": "1984.08.17"},
    {"name": "Hannah Clark", "birthday": "1992.09.02"},
    {"name": "Isaac Martinez", "birthday": "1980.10.09"},
    {"name": "Jack Rodriguez", "birthday": "1994.11.20"},
    {"name": "Karen Lewis", "birthday": "1986.12.01"},
    {"name": "Leo Walker", "birthday": "1993.02.28"},
    {"name": "Megan Hall", "birthday": "1989.03.22"},
    {"name": "Nancy Allen", "birthday": "1991.04.18"},
    {"name": "Oliver Young", "birthday": "1987.05.26"},
    {"name": "Paul Scott", "birthday": "1983.06.15"},
    {"name": "Quincy Adams", "birthday": "1992.07.12"},
    {"name": "Rita Perez", "birthday": "1980.08.04"},
    {"name": "Samuel Green", "birthday": "1990.09.16"},
    {"name": "Tina Nelson", "birthday": "1986.10.23"},
    {"name": "Uma Carter", "birthday": "1993.11.14"},
    {"name": "Victor King", "birthday": "1985.12.05"},
    {"name": "Wendy Mitchell", "birthday": "1988.01.19"},
    {"name": "Xander Carter", "birthday": "1994.02.13"},
    {"name": "Yvonne Turner", "birthday": "1984.03.28"},
    {"name": "Zachary Harris", "birthday": "1992.04.01"},
    {"name": "Aaron Lee", "birthday": "1987.05.04"},
    {"name": "Bella Cooper", "birthday": "1989.06.21"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
