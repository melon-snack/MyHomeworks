"""Homework"""
from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow
import pillow_avif
import os

register_heif_opener()

ALLOWED_EXTENSIONS: list[str] = ['jpg', 'jpeg', 'png', 'dng']



# Получение изображений
def get_images_paths(source_path: str, allowed_extensions: list[str]) -> list[str]:

# Проверка существования пути
    if not os.path.exists(source_path):
        raise ValueError("Указанный путь не существует")

    if os.path.isfile(source_path):
        return [source_path]
    
    # Папка найдена, соверщаю рекурсивный обход и собираю файлы указанных расширений
    list_paths: str = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path):
                if file.split(".")[-1] in allowed_extensions:
                    list_paths.append(full_path)
                    print(f"success! {full_path}")

    return list_paths

def compress_image(image_path: str, output_format: str, quality: int):
    supported_formats = ["webp", "heic", "avif"]
    compressed_image = Image.open(image_path)

    # Проверка формата
    if output_format not in supported_formats:
        raise ValueError (f'Формат {output_format} не поддерживается')

    #Проверка на WEBP и AVIF
    if output_format in ["webp", "avif"]:
        compressed_image.save(f"{image_path}.{output_format}", output_format=output_format, quality=quality)
        return

    if output_format == "heic":
        heif_file = heif_from_pillow(compressed_image)
        heif_file.save(f"{image_path}.{output_format}", quality=quality)
        return

def main():
    # Запрашиваю у пользователя путь к изображению/изображениям.
    user_source_path: str = input("Введите путь до изображений\n")
    # Запрашиваю у пользователя желаемый формат для конвертации.
    output_format = ""
    user_format: int = input("Выберите формат для конвертации.\nДоступные форматы: WEBP, HEIC, AVIF\n").lower()

    list_paths = get_images_paths(user_source_path, ALLOWED_EXTENSIONS)
    for image in list_paths:
        compress_image(image, user_format, 40)

main()
