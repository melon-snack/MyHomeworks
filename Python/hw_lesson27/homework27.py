"""Homework"""
from sqlite3 import Connection, connect
from tabulate import tabulate
from typing import List, Tuple, Dict, Any, Union, Optional

# Из-за особенности загрузки домашнего задания, просьба поменять пути для корректной работы
SQL_SCRIPT = "MyHomeworks\\Python\\hw_lesson27\\homework27.sql"
DB_FILE = "MyHomeworks\\Python\\hw_lesson27\\barbershop.db"

connection: Connection = connect(DB_FILE)

# Читает SQL файл и возвращает его содержимое
def read_sql_file(filepath: str) -> str:
    """
    Функция для чтения SQL файла.
    filepath: str = путь к файлу
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

# Выполняет SQL скрипт
def execute_script(conn, script: str) -> None:
    """
    Функция запуска скрипта SQL.
    conn = курсор
    script: str = путь к SQL файлу
    """
    cursor = conn.cursor()
    try:
        cursor.executescript(script)
        conn.commit()
        print('Script complete')
    except Exception as e:
        print(f"Ошибка при выполнении скрипта: {e}")
    finally:
        cursor.close()

# Поиск записей по телефону
def find_appointment_by_phone(conn, phone: str) -> list[tuple]:
    """
    Функция поиска записей по номеру телефона.
    conn = курсор
    phone: str = номер телефона для поиска
    """
    cursor = conn.cursor()
    SQL_SCRIPT = """
SELECT a.id, a.name, a.phone, a.дата, a.comment, a.status, m.first_name, m.last_name
FROM appointments a
JOIN masters m ON a.master_id = m.id
WHERE a.phone = ?;
"""
    cursor.execute(SQL_SCRIPT, (phone,))
    results = cursor.fetchall()
    cursor.close()
    return results

# Поиск записей по комменту
def find_appointment_by_comment(conn, comment_part: str) -> list[tuple]:
    """
    Функция поиска записей по комментарию.
    conn = курсор
    comment_part = комметарий для поиска (можно ввести только часть комментария)
    """
    cursor = conn.cursor()
    SQL_SCRIPT = """
SELECT a.id, a.name, a.phone, a.дата, a.comment, a.status, m.first_name, m.last_name
FROM appointments a
JOIN masters m ON a.master_id = m.id
WHERE a.comment LIKE ?;
"""

    cursor.execute(SQL_SCRIPT, (f"%{comment_part}%",))
    results = cursor.fetchall()
    cursor.close()
    return results

# Создание записи
def create_appointment(conn, client_name: str, client_phone: str, master_name: str, services_list: list[str], comment: str = None) -> int:
    """
    Создаёт запись в таблице клиентов. Возвращает ID созданной записи.
    cann - курсор
    
    client_name, client_phone, master_name, services_list, comment - данные для занесения в таблицу (слева на право: имя клиента, телефон клиента, имя мастера, услуга, коммент)
    """
    cursor = conn.cursor()
    
    # -запуск транзакции
    conn.execute("BEGIN")

    # -ищем мастера по указанному имени
    cursor.execute("SELECT id FROM Masters WHERE first_name = ?", (master_name,))
    master = cursor.fetchone()

    if not master:
        cursor.execute("ROLLBACK")
        raise ValueError(f"Мастер с именем {master_name} не найден")
    
    # -получаем ID мастера
    master_id = master[0]

    # -создаём запись в таблице Appointments
    cursor.execute(
        "INSERT INTO Appointments (name, phone, master_id, comment) VALUES (?, ?, ?, ?)", 
        (client_name, client_phone, master_id, comment)
    )

    # -получаем ID записи
    appointment_id = cursor.lastrowid

    for service_title in services_list:
        cursor.execute("SELECT id FROM Services WHERE title = ?", (service_title,))
        service = cursor.fetchone()
        if not service:
            cursor.execute("ROLLBACK")
            raise ValueError(f"Услуга {service_title} не найдена.\n")
        service_id = service[0]
        cursor.execute(
            "INSERT INTO appointments_services (appointment_id, service_id) VALUES (?, ?)",
            (appointment_id, service_id)
        )

    # -фиксация изменений
    cursor.execute("COMMIT")
    cursor.close()
    return appointment_id

# Проверка функций
if __name__ == "__main__":
    # 1й Этап
    sql_script = read_sql_file(SQL_SCRIPT)
    cursor = connection.cursor()
    execute_script(connection, sql_script)

    cursor.close()
    connection.close()

# Поиск по телефону
    phone_input = input("Введите номер телефона для поиска:\n")
    appointments = find_appointment_by_phone(connection, phone_input)
    print("Результаты:\n")
    if appointments:
        print(tabulate(appointments, headers=["ID", "Имя клиента", "Телефон", "Дата", "Комментарий", "Статус", "Имя мастера", "Фамилия мастера"], tablefmt="grid"))
    else:
        print("Записи не найдены.")

# Поиск по комментарию
    comment_input = input("Введите комментарий или его часть.\n")
    appointments = find_appointment_by_comment(connection, comment_input)
    print("Результаты:\n")
    if appointments:
        print(tabulate(appointments, headers=["ID", "Имя клиента", "Телефон", "Дата", "Комментарий", "Статус", "Имя мастера", "Фамилия мастера"], tablefmt="grid"))
    else:
        print("Записи не найдены.")

# Создание новой записи
    data = {
        "client_name": "Артём",
        "client_phone": "+7-333-333-33-33",
        "master_name": "Пётр",
        "services_list": ["Стрижка бороды"],
        "comment": "Прошу не сбривать бороду!"
    }

    try:
        appointment_id = create_appointment(
            connection,
            client_name=data["client_name"],
            client_phone=data["client_phone"],
            master_name=data["master_name"],
            services_list=data["services_list"],
            comment=data["comment"]
        )
        print(f"Запись успешно создана! ID: {appointment_id}")

    except ValueError as e:
        print(f"Ошибка данных: {e}\n Повторите ввод данных.")
