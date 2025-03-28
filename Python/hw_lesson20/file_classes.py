"""Homework part 1"""
from abc import ABC, abstractmethod
import json
import csv
import os

class AbstractFile(ABC):
    def __init__(self, file_path:str, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def append(self):
        pass

    def __str__(self):
        return f'Документ типа {self.__class__.__name__} по пути {self.file_path}'

class JsonFile(AbstractFile):

    # Функция чтения JSON файла
    def read(self) -> list[dict]:
        with open(self.file_path, "r", encoding=self.encoding) as file:
            data = json.load(file)
            return data

# Функция записи JSON файла
    def write(self, *data: dict) -> None:
        with open(self.file_path, "w", encoding=self.encoding) as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

# Функция добавления в JSON файл
    def append(self, *data: dict) -> None:
        try:
            with open(self.file_path, "r", encoding=self.encoding) as file:
                data_dump = json.load(file)
            data_dump.extend(data)
            with open(self.file_path, "w", encoding=self.encoding) as file:
                json.dump(data_dump, file, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            with open(self.file_path, "w", encoding=self.encoding) as jsonfile:
                json.dump(data, jsonfile, indent=4, ensure_ascii=False)
