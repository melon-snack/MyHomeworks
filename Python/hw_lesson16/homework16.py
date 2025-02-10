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
