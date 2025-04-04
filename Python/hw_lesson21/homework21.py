"""Homework"""
from dataclasses import dataclass, field
import json

JSON_DATA = 'MyHomeworks\\Python\\hw_lesson21\\citi.py'

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

class CitiesSerializer:
    def __init__(self, city_data: list[dict]):
        self.city_data = city_data
        self.cities = self.__create_cities()

    def __deserialize_city(self, city_dict: dict) -> City:
        instance = City(
            name=city_dict['name'],
            population=city_dict['population'],
            subject=city_dict['subject'],
            district=city_dict['district'],
            latitude=city_dict['coords']['lat'],
            longitude=city_dict['coords']['lon'],
        )

        return instance

    def __create_cities(self) -> list:
        return [self.__deserialize_city(city) for city in self.city_data]

    def get_all_cities(self) -> list[City]:
        return self.cities

# ТЕСТ
json_handler = JsonFile(JSON_DATA)
city_data = json_handler.read()
cities_serializer = CitiesSerializer(city_data)
cities = cities_serializer.get_all_cities()
print(f'{cities[0]}\n{cities[1]}\n{cities[3]}')
