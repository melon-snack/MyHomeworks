"""Homework part 2"""

from files_utils import *

json_test = [
    {
        "name": "Steve",
        "age": 23,
        "hobby": "cooking"
    },
    {
        "name": "Amy",
        "age": 20,
        "hobby": "skating"
    }
]

new_data_json = [
    {
        "name": "Dave",
        "age": 33,
        "hobby": "skydiving"
    }
]

csv_test = [
  ["name", "age", "hobby"],  # Заголовки
  ["Kyle", 23, "drawing"],
  ["Jane", 19, "gardening"],
]

new_data_csv = [
  ["Coby", 14, "videogames"]
]

txt_test = "Hello"

new_data_txt = "World!"

write_txt(txt_test, file_path="test.txt")
write_csv(csv_test, file_path="test.csv")
write_json(json_test, file_path="test.json")

append_txt(new_data_txt, file_path="test.txt")
append_csv(new_data_csv, file_path="test.csv")
append_json(new_data_json, file_path="test.json")

print("PRINTING TXT")
print(read_txt(file_path="test.txt"))
print("PRINTING CSV")
print(read_csv(file_path="test.csv"))
print("PRINTING JSON")
print(read_json(file_path="test.json"))
print("PRINTING YAML")
print(read_yaml(file_path="test.yaml"))
