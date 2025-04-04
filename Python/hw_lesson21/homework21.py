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
