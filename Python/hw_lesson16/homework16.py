"""Homework"""
from typing import Callable, Any
import csv

# Функция декоратор проверки пароля:
def password_validator(min_length=8, min_uppercase=1, min_lowercase=1, min_special_chars=1) -> Callable:
    def decorator(func: Callable[[str], str]) -> Callable[[str, str], str]:
        def wrapper (username: str, password: str) -> str:
            # Проверка длины пароля
            if len(password) < min_length:
                raise ValueError(f'пароль {password} слишком короткий!')
            lower: int = 0
            upper: int = 0
            special: int = 0
            special_characters: str = '[@_!#$%^&*()<>?|}{~:]'
            for i in password:
                # Подсчёт количеста строчных букв
                if(i.islower()):
                    lower+=1
                # Подсчёт количества заглавных букв
                elif(i.isupper()):
                    upper+=1
                # Подсчёт количества специальных символов
                elif (i in special_characters):
                    special+=1
                else:
                    continue
            # Проверка количеста заглавных букв
            if upper < min_uppercase:
                raise ValueError(f'пароль {password} содержит недостаточно заглавных букв')
            # Проверка количества строчных букв
            elif lower < min_lowercase:
                raise ValueError(f'пароль {password} содержит недостаточно строчных букв')
            # Проверка количества специальных символов
            elif special < min_special_chars:
                raise ValueError(f'пароль {password} содержит недостаточно специальных символов')
            return func(username, password)
        return wrapper
    return decorator

# Функция декоратор проверки юзернейма
def username_validator(func: Callable) -> Callable:
    def wrapper(username, password):
        if " " in username:
            raise ValueError(f"В строке {username} содержатся пробелы!")
        return func(username, password)
    return wrapper

# Функция записи в csv файл
def append_csv(*data: dict, file_path: str, delimiter=';', encoding: str ='utf-8-sig'):
    with open(file_path, "a", encoding=encoding, newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(data)

@password_validator(min_length=8, min_uppercase=1, min_lowercase=1, min_special_chars=1)
@username_validator
# Функция записи юзернейма и пароля в csv файл
def register_user(username, password):
    user: list = []
    user.append(username)
    user.append(password)
    append_csv(user, file_path="users.csv")

# Проверка успешного юзернейма и пароля
try:
    register_user("Bob", "qW@rT1uI")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Проверка на ошибку отсутствия заглавных букв
try:
    register_user("Bob", "qw@rt1ui")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Проверка на ошибку отсутствия прописных букв
try:
    register_user("Bob", "QW@RT1UI")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Проверка на ошибку отсутствия специальных символов
try:
    register_user("Bob", "qWerT1uI")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Проверка ошибки юзернейма
try:
    register_user("Bob Bobbert", "qW@rT1uI")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Проверка записи в csv файл
register_user("Bob", "qW@rT1uI")
