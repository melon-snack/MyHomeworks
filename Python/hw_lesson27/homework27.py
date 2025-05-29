"""Homework"""
from sqlite3 import Connection, connect
from tabulate import tabulate
from typing import List, Tuple, Dict, Any, Union, Optional

# Из-за особенности загрузки домашнего задания, просьба поменять пути для корректной работы
SQL_SCRIPT = "MyHomeworks\\Python\\hw_lesson27\\homework27.sql"
DB_FILE = "MyHomeworks\\Python\\hw_lesson27\\barbershop.db"

connection: Connection = connect(DB_FILE)