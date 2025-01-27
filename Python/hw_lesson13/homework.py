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
