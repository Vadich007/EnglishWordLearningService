import random

DICTIONARY_CSV = "./data/words.csv"

def take_data_from_csv() -> dict:
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

def add_data_to_csv(english_word, russian_word) -> None:
    new_term_line = f"{english_word};{russian_word}"
    
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
