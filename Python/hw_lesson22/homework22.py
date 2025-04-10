"""Homework"""
from dataclasses import dataclass, field
import json
import random

JSON_DATA = 'MyHomeworks\\Python\\hw_lesson22\\cities.json' # Необходимо указать путь на cities.json для корректной работы

# Класс для чтения json файлов
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

"""
Датакласс для хранения информации полученной из cities.json.
Также проверяет если name является строкой и population не является нулём,
иначе выдаёт ошибку.
"""
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

# Класс, создающий внутренний список экземпляров
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

class CityGame:
    def __init__(self, cities_serializer: CitiesSerializer):
        """
        Инициализирует игру на основе списка городов.

        :param cities_serializer: Сериализатор, содержащий список объектов City.
        """
        self.cities = cities_serializer.get_all_cities()
        self.cities_used = set()
        self.current_city = None

    def human_turn(self, city_input: str) -> bool:
        """
        Обрабатывает ход человека: проверяет корректность введенного названия и обновляет состояние.

        :param city_input: Название города, введенное игроком.
        :return: True, если ход корректен, иначе False.
        """
        city_input = city_input.strip().capitalize()

        if not city_input:
            print("Ошибка! Название города - пустое.")
            return False

        if self.current_city and not city_input.startswith(self.current_city[-1].upper()):
            print(f"Ошибка! Город должен начинаться на букву '{self.current_city[-1].upper()}'.")
            return False

        city = next((c for c in self.cities if c.name == city_input), None)
        if not city:
            print("Ошибка. В базе нет такого города.")
            return False

        if city.is_used:
            print("Ошибка! Этот город уже использован.")
            return False

        city.is_used = True
        self.cities_used.add(city.name)
        self.current_city = city.name
        return True

    def computer_turn(self) -> str:
        """
        Находит подходящий город для хода компьютера и обновляет состояние игры.

        :return: Название города, выбранного компьютером.
        """
        if not self.current_city:
            # Если это первый ход, компьютер выбирает случайный город
            check_cities = [city for city in self.cities if not city.is_used]
        else:
            # Иначе, компьютер выбирает город, начинающийся на последнюю букву предыдущего города
            last_char = self.current_city[-1].upper()
            check_cities = [city for city in self.cities if not city.is_used and city.name.startswith(last_char)]

        if not check_cities:
            return ""

        com_city_pick = random.choice(check_cities)
        com_city_pick.is_used = True
        self.cities_used.add(com_city_pick.name)
        self.current_city = com_city_pick.name
        return com_city_pick.name

    def check_game_over(self) -> bool:
        """
        Проверяет наличие возможных ходов и определяет завершение игры.

        :return: True, если игра завершена, иначе False.
        """
        if not self.current_city:
            return False

        last_char = self.current_city[-1].upper()
        check_cities = [city for city in self.cities if not city.is_used and city.name.startswith(last_char)]
        return len(check_cities) == 0
