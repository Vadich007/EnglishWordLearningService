import random
import csv

DICTIONARY_CSV = "./data/words.csv"
STATISTIC_CSV = "./data/statistic.csv"

def take_data_from_dictionary() -> dict:
    letters = {}
    
    with open(DICTIONARY_CSV, "r", encoding="utf-8") as f:
        for row in f.readlines():
            words = row.split(',')
            letter = words[0][0].upper()
            if letter not in letters:
                letters[letter] = []
            letters[letter].append([words[0], words[1]])

    return dict(sorted(letters.items()))

def dictionary_contain(endlish_word) -> bool:
    existing_terms= []

    with open(DICTIONARY_CSV, "r", encoding="utf-8") as f:
        for l in f.readlines():
            existing_terms = l.split(",")[0]

    if endlish_word in existing_terms:
        return True
    return False

def add_data_to_dictionary(english_word, russian_word) -> None:
    new_term_line = f"{english_word},{russian_word}"
    
    with open(DICTIONARY_CSV, "a", encoding="utf-8") as f:
        f.write("\n" + new_term_line)

def get_random_word():
    existing_terms= []

    with open(DICTIONARY_CSV, "r", encoding="utf-8") as f:
        for l in f.readlines():
            existing_terms.append(l.split(",")[0])
    
    return random.choice(existing_terms)

def get_russian(english:str):
    ans = ""
    with open(DICTIONARY_CSV, "r", encoding="utf-8") as f:
        for l in f.readlines():
            if l.split(",")[0] == english:
                ans = l.split(",")[1].strip("\n")
                break

    return ans

def get_total_words():
    with open(DICTIONARY_CSV, "r", encoding="utf-8") as f:
        return len(f.readlines())
    
def get_total_success():
    with open(STATISTIC_CSV, "r", encoding="utf-8") as f:
        for l in f.readlines():
            if l.split(',')[0] == "total_success":
                return int(l.split(',')[1].strip("\n"))
    
    return 0

def get_total_fail():
    with open(STATISTIC_CSV, "r", encoding="utf-8") as f:
        for l in f.readlines():
            if l.split(',')[0] == "total_fail":
                return int(l.split(',')[1].strip("\n"))
    
    return 0

def add_statistic(name):
    stat = {}

    with open(STATISTIC_CSV, "r", encoding="utf-8") as f:
        for l in f.readlines():
            col = l.split(',')[0]
            value = l.split(',')[1].strip("\n")
            stat[col] = value

    stat[name] = int(stat[name]) + 1

    with open(STATISTIC_CSV, "w", encoding="utf-8") as f:
        for s in stat:
            f.write(f"{s},{stat[s]}\n")