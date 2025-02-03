"""Homework part 1"""
import json

# Функция чтения данных файла JSON
def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, "r", encoding=encoding) as jsonfile:
        data = json.load(jsonfile)
        return data
