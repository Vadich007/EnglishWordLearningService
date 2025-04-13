"""Модуль для работы со статистикой."""

from . import csv_utils

def get_statistic():
    """Получение статистики викторины."""
    result = {}
    total_fail = csv_utils.get_total_fail()
    total_success = csv_utils.get_total_success()
    result["total_words"] = csv_utils.get_total_words()
    result["total_success"] = total_success
    result["total_fail"] = total_fail
    if total_fail + total_success != 0:
        result["percent_success"] = round(total_success / (total_success + total_fail) * 100)
    else:
        result["percent_success"] = 0
    result["percent_success"] = str(result["percent_success"]) + "%"

    return result
