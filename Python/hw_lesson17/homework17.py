"""Homework"""
# 1 импорт full_dict из marvel.py
from marvel import full_dict

# 2 ввод от пользователя
user_ids = input("Введите цифры через пробел\n")
user_ids = user_ids.split()
user_ids = list(map(lambda num: int(num) if num.isdigit() else None, user_ids))

# 3 перепаковка full_dict в список словарей
full_list = [{"id": film_id, **film} for film_id, film in full_dict.items()]

# 4 список, содержащий id c номерами пользователя
def get_user_list(ids):
    if not ids is None:
        ids_index = full_list.index(ids)
        return ids_index in user_ids
user_list = list(filter(get_user_list, full_list))

# 5 создание множества с помощью set comprehension
director_set = {film[val] for film in full_list for val in film if val == "director"}

# 7 фильтр фильмов из full_dict начинающихся на букву Ч
def get_letter(film):
    if not film["title"] == None:
        return "Ч" in film["title"]

letter_list = list(filter(get_letter, full_list))

# 8 сортировка словаря full_dict по одному параметру с помощью lambda
# сортировка по году выхода
sort_first = full_list
sort_first.sort(key=lambda film: (film["year"] if isinstance(film["year"], int) else 0))

# 9 сортировка словаря full_dict по двум параметрам с помощью lambda
# сортировка по году выхода и названию
sort_second = full_list
sort_second.sort(
    key=lambda film: (
        film["year"] if isinstance(film["year"], int) else 0,
        film["title"] if film["title"] else "Без Названия",
    )
)

# 10 однострочник фильтр и сортировщик
# сортировка фильмов по названию из 2017 года
sort_third = list(sorted(filter(lambda film: film["year"] == 2017, full_list),key=lambda film: film["title"],))
