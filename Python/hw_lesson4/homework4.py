"""Homework"""
name_input = input("Введите ваше имя\n")
grade_input = input("Введите вашу оценку:\n ")
if grade_input.isdigit():
    grade = int(grade_input)
    if grade < 1 or grade > 12:
        print("Введено некорректное значение. Значение должно быть не меньше 1 и не больше 12")
    elif grade >= 1 and grade <= 3:
        student_level = "Начальный"
        print(f'Имя студента: {name_input}. Уровень: {student_level}')
    elif grade >= 4 and grade <= 6:
        student_level = "Средний"
        print(f'Имя студента: {name_input}. Уровень: {student_level}')
    elif grade >= 7 and grade <= 9:
        student_level = "Достаточный"
        print(f'Имя студента: {name_input}. Уровень: {student_level}')
    elif grade >= 10 and grade <= 12:
        student_level = "Высокий"
        print(f'Имя студента: {name_input}. Уровень: {student_level}')
else:
    print("Введено некорректное значение. Пожалуйста, введите число.")
