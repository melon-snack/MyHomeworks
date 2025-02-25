"""Homework"""
import json
import csv

# Класс работы с TXT файлами
class TxtFileHandler:
    def __init__(self):
        pass

# Функция чтения TXT файла
    def read_file(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                read_file = file.read()
                return read_file
        except FileNotFoundError:
            return ""
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Функция записи TXT файла
    def write_file(self, filepath: str, *data: str):
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                text = "".join(*data)
                file.write(text)
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Функция добавления в TXT файл
    def append_file(self, filepath: str, *data: str, ):
        try:
            with open(filepath, "a", encoding="utf-8") as file:
                file.write("\n")
                text = "".join(*data)
                file.write(text)
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")
