import re

def is_russian(word) -> bool:
    return bool(re.fullmatch(r'^[А-Яа-яЁё]+$', word))

def is_english(word) -> bool:
    return bool(re.fullmatch(r'^[A-Za-z\'\-]+$', word))