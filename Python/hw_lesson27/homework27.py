"""Homework"""
from sqlite3 import Connection, connect
from tabulate import tabulate
from typing import List, Tuple, Dict, Any, Union, Optional

# Из-за особенности загрузки домашнего задания, просьба поменять пути для корректной работы
SQL_SCRIPT = "non_git\\homework\\homework.sql"
DB_FILE = "non_git\\homework\\barbershop.db"

connection: Connection = connect(DB_FILE)