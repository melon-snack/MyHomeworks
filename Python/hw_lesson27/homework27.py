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
