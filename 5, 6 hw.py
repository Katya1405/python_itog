import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)


def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        logging.error("Error occurred: %s" % str(e))


divide(10, 0)

# Задание 2
import logging
import functools

logging.basicConfig(filename='logs.log', level=logging.INFO)


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Function: {func.__name__}, Args: {args}, kwargs: {kwargs}, Result: {result}")
        return result

    return wrapper


@logger
def add(x, y):
    return x + y


add(1, 2)
add(2, 3)

# Задание 3

import logging

import functools

logging.basicConfig(filename='logs.log', level=logging.INFO,

                    format='%(levelname)s %(asctime)s %(name)s %(message)s')


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Function: {func.__name__}")
        logging.info(f"Args: {args}")
        logging.info(f"Kwargs: {kwargs}")
        logging.info(f"Result: {result}")
        return result

    return wrapper


@logger
def add(x, y):
    return x + y


add(1, 2)
add(2, 3)

# Задание 4
import datetime


def get_weekday(weekday):
    weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    if isinstance(weekday, str):

        try:

            weekday = weekdays.index(weekday.lower())

        except ValueError:

            raise ValueError("Неверное значение дня недели")

    if not 0 <= weekday <= 6:
        raise ValueError("Неверное значение дня недели")

    return weekday


# Задание 5

def get_month(month):
    months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
              "декабрь"]

    if isinstance(month, str):

        try:

            month = months.index(month.lower()) + 1

        except ValueError:

            raise ValueError("Неверное значение месяца")

    if not 1 <= month <= 12:
        raise ValueError("Неверное значение месяца")

    return month


# Задание 6
def parse_date(date_str):
    parts = date_str.split()

    if len(parts) != 4:
        raise ValueError("Неверный формат даты")

    day = parts[0]

    if day[-2:] == "го":

        day = int(day[:-2])

    elif day[-1:] == "-":

        day = int(day[:-1])

    else:

        raise ValueError("Неверное значение дня")

    weekday = get_weekday(parts[1])

    month = get_month(parts[3])

    current_year = datetime.datetime.now().year

    try:

        date = datetime.datetime(current_year, month, day)

    except ValueError:

        raise ValueError("Неверная дата")

    if date.weekday() != weekday:
        raise ValueError("Неверный день недели")

    return date


import sys

if __name__ == "__main__":

    date_str = " ".join(sys.argv[1:])

    try:

        date = parse_date(date_str)

        print(date.strftime("%d.%m.%Y"))

    except ValueError as e:

        print(f"Ошибка: {e}")