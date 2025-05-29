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
