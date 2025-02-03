"""Homework part 1"""
import json
import csv

# Функция чтения данных файла JSON
def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, "r", encoding=encoding) as jsonfile:
        data = json.load(jsonfile)
        return data

# Функция записи данных в JSON файл
def write_json(*data: dict, file_path: str, encoding: str = "utf-8"):
    with open(file_path, "w", encoding=encoding) as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

# Функция чтения данных файла CSV
def read_csv(file_path: str, delimiter=';', encoding: str ='utf-8-sig'):
    with open(file_path, "r", encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        result = list(reader)
    return result

# Функция записи данных файла CSV
def write_csv(*data: dict, file_path: str, delimiter=';', encoding: str ='utf-8-sig'):
    with open(file_path, "w", encoding=encoding, newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

# Функция изменения данных CSV файла
def append_csv(*data: dict, file_path: str, delimiter=';', encoding: str ='utf-8-sig'):
    with open(file_path, "a", encoding=encoding, newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(data)

# Функция чтения данных файла TXT
def read_txt(file_path: str, encoding: str = "utf-8"):
    with open(file_path, "r", encoding=encoding) as file:
        read_file = file.read()
        return read_file

# Функция запись данных файла TXT
def write_txt(*data: str, file_path: str, encoding: str = "utf-8"):
    with open(file_path, "w", encoding=encoding) as file:
        text = " ".join(*data)
        file.write(text)

# Функция изменения данных файла TXT
def append_txt(*data: str, file_path: str, encoding: str = "utf-8"):
    with open(file_path, "a", encoding=encoding) as file:
        file.write("\n")
        text = " ".join(*data)
        file.write(text)
