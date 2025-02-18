"""Homework"""
# 1 импорт full_dict из marvel.py
from marvel import full_dict

# 2 ввод от пользователя
user_ids = input("Введите цифры через пробел\n")
user_ids = user_ids.split()
user_ids = list(map(lambda num: int(num) if num.isdigit() else None, user_ids))
