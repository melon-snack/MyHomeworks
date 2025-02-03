"""Homework part 1"""
import json

# Функция чтения данных файла JSON
def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, "r", encoding=encoding) as jsonfile:
        data = json.load(jsonfile)
        return data

# Функция записи данных в JSON файл
def write_json(*data: dict, file_path: str, encoding: str = "utf-8"):
    with open(file_path, "w", encoding=encoding) as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)
