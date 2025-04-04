"""Homework"""
from dataclasses import dataclass, field
import json

JSON_DATA = 'MyHomeworks\\Python\\hw_lesson21\\homework21.py'

class JsonFile:
    def __init__(self, file_path: str, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def read(self) -> list[dict]:
        try:
            with open(self.file_path, "r", encoding=self.encoding) as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

@dataclass
class City:
    name: str = field(compare=False)
    population: int 
    subject: str = field(compare=False)
    district: str = field(compare=False)
    latitude: float = field(compare=False)
    longitude: float = field(compare=False)
    is_used: bool = field(compare=False, default=False, init=False)

    def __post_init__(self):
        self.__validate_name()
        self.__validate_population()

    def __validate_name(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError('Name должен быть строкой и не пустым')

    def __validate_population(self):
        if not isinstance(self.population, int) or self.population <= 0:
            raise ValueError('Population должно содержать положительное число')
