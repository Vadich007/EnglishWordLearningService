from django.shortcuts import render
from django.core.cache import cache
import csv

def index(request):
    return render(request, "index.html")

def dictionary(request):
    letters = {}
    
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            letter = row['english'][0].upper()
            if letter not in letters:
                letters[letter] = []
            letters[letter].append([row["english"], row["russian"]])

    return render(request, 'dictionary.html', {'letters': dict(sorted(letters.items()))})