"""
    Модуль обрабатывает поступающие запросы и возвращает html-страницы.
"""

import json
from django.shortcuts import render
from django.http import JsonResponse
from . import csv_utils
from . import validator
from . import statistic

def index(request):
    """
    Вывод основной страницы.
    """
    return render(request, "index.html")

def dictionary(request):
    """
    Вывод словаря.
    """
    letters = csv_utils.take_data_from_dictionary()
    return render(request, 'dictionary.html', {'letters': letters})

def add_word(request):
    """
    Вывод формы добавления слов.
    """
    return render(request, 'add_word.html')

def send_word(request):
    """
    Обработчик запроса на добавление слова.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        english_word = data['englishWord']
        russian_word = data['russianWord']

        if not validator.is_english(english_word):
            return JsonResponse({'status': 'error',
                                 'message': 'Неверный формат английского слова'},
                                 status=400)
        elif not validator.is_russian(russian_word):
            return JsonResponse({'status': 'error',
                                 'message': 'Неверный формат русского слова'},
                                 status=400)
        elif csv_utils.dictionary_contain(english_word):
            return JsonResponse({'status': 'error',
                                 'message': 'Слово уже содержится в словаре'},
                                 status=400)
        else:
            csv_utils.add_data_to_dictionary(english_word, russian_word)
            return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'error': 'Invalid method'}, status=405)

def quiz(request):
    """
    Вывод страницы викторины.
    """
    return render(request, 'quiz.html')

def check(request):
    """
    Проверка правильности угаданного слова.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'russian': csv_utils.get_russian(data["english"])})

    return JsonResponse({'error': 'Invalid method'}, status=405)

def random(request):
    """
    Отправка случайного слова из словаря.
    """
    if request.method == 'GET':
        return JsonResponse({'english': csv_utils.get_random_word()})

    return JsonResponse({'error': 'Invalid method'}, status=405)

def stat(request):
    """
    Вывод страницы с статистикой.
    """
    return render(request, 'stat.html', statistic.get_statistic())

def add_stat(request):
    """
    Добавление статистики во время викторины.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        csv_utils.add_statistic(data["stat"])
        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'error': 'Invalid method'}, status=405)
