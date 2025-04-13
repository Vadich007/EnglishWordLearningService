from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
import json
from . import csv_utils
from . import validator
from . import statistic

def index(request):
    return render(request, "index.html")

def dictionary(request):
    letters = csv_utils.take_data_from_dictionary()
    return render(request, 'dictionary.html', {'letters': letters})

def add_word(request):
    return render(request, 'add_word.html')

def send_word(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        english_word = data['englishWord']
        russian_word = data['russianWord']
        
        if not validator.is_english(english_word):
            return JsonResponse({'status': 'error', 'message': 'Неверный формат английского слова'}, status=400)
        elif not validator.is_russian(russian_word): 
            return JsonResponse({'status': 'error', 'message': 'Неверный формат русского слова'}, status=400)
        elif csv_utils.dictionary_contain(english_word):
            return JsonResponse({'status': 'error', 'message': 'Слово уже содержится в словаре'}, status=400)
        else:
            csv_utils.add_data_to_dictionary(english_word, russian_word)
            return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'error': 'Invalid method'}, status=405)

def quiz(request):
    return render(request, 'quiz.html')
    
def check(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'russian': csv_utils.get_russian(data["english"])})

    return JsonResponse({'error': 'Invalid method'}, status=405)
    
def random(request):
    if request.method == 'GET':
        return JsonResponse({'english': csv_utils.get_random_word()})

    return JsonResponse({'error': 'Invalid method'}, status=405)
        
def stat(request):
    return render(request, 'stat.html', statistic.get_statistic())

def add_stat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        csv_utils.add_statistic(data["stat"])
        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'error': 'Invalid method'}, status=405)