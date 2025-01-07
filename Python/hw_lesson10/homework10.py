"""Homework"""

small_dict = {
    'Человек-муравей и Оса: Квантомания': 2023,
    'Стражи Галактики. Часть 3': 2023,
    'Капитан Марвел 2': 2023,
    'Дэдпул 3': 2024,
    'Капитан Америка: Дивный новый мир': 2024,
    'Громовержцы': 2024,
    'Блэйд': 2025,
    'Фантастическая четвёрка': 2025,
    'Мстители: Династия Канга': 2026,
    'Мстители: Секретные войны': 2027,
    'Безымянный фильм о Человеке-пауке': None,
    'Безымянный фильм о Шан-Чи': None,
    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

items_dict = small_dict.items()


# Задача 1: Поиск фильмов по названию
results = []
search_input = input('Введите название фильма\n')

for film, year in items_dict:
    if search_input == "" or search_input is None:
        break
    elif search_input.lower() in film.lower():
        if year is None:
            results.append(f'{film}: TBA')
        else:
            results.append(f'{film}: {year}')
if not results:
    print("Такого фильма нет")
else:
    print("Результат:")
    print(*results, sep='\n')

input("для продолжения программы нажмите клавишу Enter")
# Задача 2: Фильтрация фильмов по году выхода
results_2024 = []
dict_2024 = {}
results_dict_2024 = []

print("Распечатанные названия фильмов:")
for film, year in items_dict:
    if year is None:
        continue
    elif year > 2024:
        # Распечатывание названий фильмов
        print(f'{film}: {year}')
        results_2024.append(film)
        dict_2024[film] = year
        results_dict_2024.append({film: year})
# Cписок названий фильмов
print("Список:")
print(*results_2024, sep='\n')
# Словарь фильмов после 2024
print("Словарь:")
print(dict_2024)
# Список словарей фильмов после 2024
print("Список словарей:")
print(*results_dict_2024, sep='\n')
