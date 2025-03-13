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
