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
