"""Homework"""
from abc import ABC, abstractmethod

class PalindromeStrategy(ABC):
    @abstractmethod
    def is_palindrome(self, text: str) -> bool:
        pass

class SingleWordPalindrome(PalindromeStrategy):

    def is_palindrome(self, text: str) -> bool:
        reversed_text = text[::-1]
        return text.lower() == reversed_text.lower()

class MultiWordPalindrome(PalindromeStrategy):

    def is_palindrome(self, text:str) -> bool:
        reversed_text = text[::-1]
        return "".join(text.split()).lower() == "".join(reversed_text.split()).lower()

class PalindromeContext:

    def __init__(self, strategy: PalindromeStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PalindromeStrategy) -> None:
        self._strategy = strategy

    def check(self, text: str) -> bool:
        return self._strategy.is_palindrome(text)
