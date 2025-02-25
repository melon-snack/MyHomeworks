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

# Класс работы с CSV файлами
class CSVFileHandler:
    def __init__(self):
        pass

# Функция чтения CSV файла
    def read_file(self, filepath: str):
        try:
            with open(filepath, "r", encoding='utf-8-sig') as file:
                reader = csv.reader(file, delimiter=';')
                result = list(reader)
            return result
        except FileNotFoundError:
            return []
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Функция записи CSV файла
    def write_file(self, filepath: str, *data: dict):
        try:
            with open(filepath, "w", encoding='utf-8-sig', newline="") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerows(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Функция добавления в CSV файл
    def append_file(self, filepath: str, *data: dict):
        try:
            with open(filepath, "a", encoding='utf-8-sig', newline="") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Класс работы с JSON файлами
class JSONFileHandler:
    def __init__(self):
        pass

# Функция чтения JSON файла
    def read_file(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as jsonfile:
                data = json.load(jsonfile)
                return data
        except FileNotFoundError:
            return []
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Функция записи JSON файла
    def write_file(self, filepath: str, *data: dict):
        try:
            with open(filepath, "w", encoding="utf-8") as jsonfile:
                json.dump(data, jsonfile, indent=4, ensure_ascii=False)
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Функция добавления в JSON файл
    def append_file(self, filepath: str, *data: dict):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data_dump = json.load(file)
            data_dump.extend(data)
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(data_dump, file, indent=4, ensure_ascii=False)
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {filepath}")

# Работа с TXT файлами
txt_handler = TxtFileHandler()
txt_handler.write_file("example.txt", "Начало файла.\n")
txt_handler.append_file("example.txt", "Добавляем строку.\n")
content_txt = txt_handler.read_file("example.txt")
print("Содержимое TXT:\n", content_txt)

# Работа с CSV файлами
csv_handler = CSVFileHandler()
data_csv = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
csv_handler.write_file("example.csv", data_csv)
csv_handler.append_file("example.csv", [{'name': 'Charlie', 'age': '35'}])
content_csv = csv_handler.read_file("example.csv")
print("Содержимое CSV:\n", content_csv)

# Работа с JSON файлами
json_handler = JSONFileHandler()
data_json = [{'product': 'Laptop', 'price': 1500}, {'product': 'Phone', 'price': 800}]
json_handler.write_file("example.json", data_json)
json_handler.append_file("example.json", [{'product': 'Tablet', 'price': 600}])
content_json = json_handler.read_file("example.json")
print("Содержимое JSON:\n", content_json)
