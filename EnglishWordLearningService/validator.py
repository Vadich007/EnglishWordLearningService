"""Модуль для валидации строк."""

import re

def is_russian(word) -> bool:
    """Валидация русских слов."""
    return bool(re.fullmatch(r'^[А-Яа-яЁё]+$', word))

def is_english(word) -> bool:
    """Валидация английских слов."""
    return bool(re.fullmatch(r'^[A-Za-z\'\-]+$', word))
