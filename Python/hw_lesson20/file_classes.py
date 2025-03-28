"""Homework part 1"""
from abc import ABC, abstractmethod
import json
import csv
import os

class AbstractFile(ABC):
    def __init__(self, file_path:str, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

# Абстрактная функция чтения
    @abstractmethod
    def read(self):
        pass

# Абстрактная функция записи
    @abstractmethod
    def write(self):
        pass

# Абстрактная функция изменения
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

class TxtFile(AbstractFile):

# Функция чтения txt файла
    def read(self) -> list[str]:
        try:
            with open(self.file_path, "r", encoding=self.encoding) as file:
                clear_data = [string.strip() for string in file.readlines()]
                return clear_data
        except FileNotFoundError:
            return ""

# Функция записи txt файла
    def write(self, *data:str) -> None:
        with open(self.file_path, "w", encoding=self.encoding) as file:
            write_data = "\n".join(data)
            file.write(write_data)

# Функция добавления в txt файл
    def append(self, *data:str) -> None:
        with open(self.file_path, "a", encoding=self.encoding) as file:
            if os.path.isfile(self.file_path):
                file.write("\n")
                write_data = "\n".join(data)
                file.write(write_data)
            else:
                write_data = "\n".join(data)
                file.write(write_data)

class CSVFile(AbstractFile):
    def __init__(self, file_path, encoding="utf-8-sig"):
        super().__init__(file_path)
        self.encoding = encoding

    fields = ['name', 'age']

# Функция чтения CSV файла
    def read(self):
        try:
            with open(self.file_path, "r", encoding=self.encoding) as file:
                reader = csv.DictReader(file, delimiter=';')
                result = list(reader)
            return result
        except FileNotFoundError:
            return []

# Функция записи CSV файла
    def write(self, data:list[dict]):
        with open(self.file_path, "w", encoding=self.encoding, newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields, delimiter=';')
            writer.writeheader()
            writer.writerows(data)

# Функция добавления в CSV файл
    def append(self, data:list[dict]):
        with open(self.file_path, "a", encoding=self.encoding) as file:
            if os.path.isfile(self.file_path):
                writer = csv.DictWriter(file, fieldnames=self.fields, delimiter=';')
                writer.writerows(data)
            else:
                writer = csv.DictWriter(file, fieldnames=self.fields, delimiter=';')
                writer.writeheader()
                writer.writerows(data)
