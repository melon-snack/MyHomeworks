"""Homework"""
ENG = 'abcdefghijklmnopqrstuvwxyz'
RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
LOOP = [122, 96, 1103, 1071]
result_text = ""

input_string = input("Введите текст на английском или русском используя ТОЛЬКО буквы\n").lower()
if input_string == "":
    input("Ошибка, вы ничего не ввели. Перезапустите программу и попробуйте снова.\n")
    quit()
input_move = input("Введите число на которое сдвигается буква\n")
if not input_move.isdigit():
    input("Ошибка, вы ввели не число. Перезапустите программу и попробуйте снова.\n")
    quit()
input_move = int(input_move)

print("проверяю текст на содержание недопустимых символов...")
for letter in input_string:
    if letter == " ":
        continue
    elif not letter in ENG:
        if not letter in RUS:
            print(f'Вы ввели нечитаемый символ "{letter}".')
            input("Ошибка, найден нечитаемый символ. Перезапустите программу и попробуйте снова.\n")
            quit()
print("символы не найдены, шифрую текст...")
# проверяет текст на наличие цифр и спец символов.
# если такой символ найден, то он выводится и программа останавливается.

for letter in input_string:
    if letter == " ":
        result_text += letter
        continue
    letter_take = ord(letter)
    if letter_take == LOOP[0]:
        letter_move = LOOP[1] + input_move
    elif letter_take == LOOP[2]:
        letter_move = LOOP[3] + input_move
# проверяет, является ли буква, последней буквой алфавита
# если да, то начинает отсчёт с начала алфавита.
    elif letter_take == 1105:
        letter_move = 1077 + input_move
# заменяет букву ё на е.
    else:
        letter_move = letter_take + input_move
    result_letter = chr(letter_move)
    result_text += result_letter
print(result_text)
