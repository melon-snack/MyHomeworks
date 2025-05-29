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
