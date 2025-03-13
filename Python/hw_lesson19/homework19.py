"""Homework"""
import os
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.webp')

    def __init__(self, user_quality:int):
        self.__quality:int = self.__validate_quality(user_quality)

# Проверяет, указанное качество, если оно int и больше 0
# Если да то выдаёт качество по-умолчанию (50)
    def __validate_quality(self, quality:int):
        try:
            quality = int(quality)
        except TypeError:
            print("Указано не числовое значение, выставляю качество по-умолчанию (50)\n")
            return False
        if quality < 0:
            print("Указано отрицательное качество, выставляю качество по-умолчанию (50)\n")
            return False

# Setter, устанавливающий качество сжатия
    def quality_set(self, quality:int):
        self.__validate_quality(quality)
        if self.__validate_quality(quality) is False:
            self.__quality = 50
        else:
            self.__quality = quality
        return self.__quality

# Getter, который берёт качество сжатия
    def quality_get(self) -> int:
        return self.__quality

# Сжимает изображение и сохраняет его в формате HEIF
    def compress_image(self, input_path:str, output_path:str) -> None:
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=50)
        print(f"Сжато: {input_path} -> {output_path}")

# Функция, обрабатывающая все изображения в указанной директории и её поддиректориях
    def process_directory(self, directory: str) -> None:
        for root, _, files in os.walk(directory):
            for file in files:
            # Проверяем расширение файла
                print(f'Проверяем расширение файла {file}')
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)
                else:
                    print(f'Файл {file} не поддерживается.\n')
                    continue

# Основная функция программы. Обрабатывает входной путь и запускает сжатие изображений
def main(input_path: str) -> None:
    register_heif_opener()
    input_path = input_path.strip('"')  # Удаляем кавычки, если они есть

# Принимает качество от пользователя и запускает ImageCompressor
    user_quality = input("Введите нужное качество изображения\n По умолчанию - 50\n")
    print(f'Запускается ImageCompressor с указанным качеством {user_quality}')
    compress = ImageCompressor(user_quality)

    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            # Если указан путь к файлу, обрабатываем только этот файл
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + '.heic'
            compress.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            # Если указан путь к директории, обрабатываем все файлы в ней
            print(f"Обрабатываем директорию: {input_path}")
            compress.process_directory(input_path)
            # Функция process_directory рекурсивно обойдет все поддиректории
            # и обработает все поддерживаемые изображения
    else:
        print("Указанный путь не существует")

# Запуск main
if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории:\n")
    main(user_input)

