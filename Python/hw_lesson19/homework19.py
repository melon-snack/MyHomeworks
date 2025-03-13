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
