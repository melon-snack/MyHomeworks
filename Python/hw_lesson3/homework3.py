"""Homework"""

# Задание №1: Конвертация секунд
input_seconds = int(input("Введите количество секунд\n"))
result_seconds = input_seconds % 60
minutes_get = input_seconds // 60
result_minutes = minutes_get % 60
result_hours = minutes_get // 60

print(f'В указанном количестве секунд ({input_seconds}):\nЧасов: {result_hours}\nМинут: {result_minutes}\nСекунд: {result_seconds}')

# Задание №2: Конвертация температуры
input_temp_celsius = int(input("Введите температуру в градусах Цельсия:\n"))
temp_kelvin = input_temp_celsius + 273.15
temp_fahrenheit = (input_temp_celsius * 9 / 5) + 32
temp_reaumur = input_temp_celsius * 4 / 5

print(f'Цельсий: {round(input_temp_celsius, 2)} °C\nКельвин: {round(temp_kelvin, 2)} K\nФаренгейт: {round(temp_fahrenheit, 2)} °F\nРеомюр: {round(temp_reaumur, 2)} °Ré')
