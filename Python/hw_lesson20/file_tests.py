"""Homework part 2"""
from file_classes import JsonFile, TxtFile, CSVFile

if __name__ == "__main__":
    data_json = [{'product': 'Laptop', 'price': 1500}, {'product': 'Phone', 'price': 800}]
    document_json = JsonFile("test.json")
    document_json.write(data_json)
    print(document_json.read())
    document_json.append([{'name': 'Charlie', 'age': '35'}])
    print(document_json.read())

    document_txt = TxtFile("test.txt")
    document_txt.write("Hello", "World")
    print(document_txt.read())
    document_txt.append("And", "Goodbye!")
    print(document_txt.read())

    data_csv: list[dict] = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    new_data_csv: list[dict] = [{'name': 'Charlie', 'age': '35'}]
    document_csv = CSVFile("test.csv")
    document_csv.write(data_csv)
    print(document_csv.read())
    document_csv.append(new_data_csv)
    print(document_csv.read())
