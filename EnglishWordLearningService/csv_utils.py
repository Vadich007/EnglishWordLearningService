import csv

DICTIONARY_CSV = "./data/words.csv"

def take_data_from_csv() -> dict:
    letters = {}
    
    with open(DICTIONARY_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            letter = row['english'][0].upper()
            if letter not in letters:
                letters[letter] = []
            letters[letter].append([row["english"], row["russian"]])

    return dict(sorted(letters.items()))

def dictionary_contain(endlish_word) -> bool:
    existing_terms= []

    with open(DICTIONARY_CSV, "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]

    if endlish_word in existing_terms:
        return True
    return False

def add_data_to_csv(english_word, russian_word) -> None:
    new_term_line = f"{english_word};{russian_word}"
    
    with open(DICTIONARY_CSV, "a", encoding="utf-8") as f:
        f.write("\n" + new_term_line)