from collections import Counter
import re
import random

# Analizowanie danego tekstu pod kątem łączenia się następujących po sobie słów w bigramy i trigramy
# oraz utworzenie na podstawie próbki 10 zdań z dodatkowymi ograniczeniami logicznymi.

# Przykładowy plik w test/corpus.txt
file_path = input()
f = open(file_path, 'r', encoding="utf-8")  # Otworzenie pliku próbki

# Odczytanie danych z pliku i jego podział na pojedyńcze słowa

corpus = f.read()
brake_corpus = corpus.split()
new_corpus = []
for i in range(0, len(brake_corpus)-2):  # Tworzenie listy trigramów na podstawie tekstu źródłowego
    new_corpus.append([brake_corpus[i], brake_corpus[i+1], brake_corpus[i+2]])


markov_corpus = {}
for x in range(len(new_corpus)):  # Tworzenie łańcucha markova za pomocą słownika
    markov_corpus.setdefault(new_corpus[x][0] + " " + new_corpus[x][1], [])
    markov_corpus[new_corpus[x][0] + " " + new_corpus[x][1]].append(new_corpus[x][2])

for x, y in markov_corpus.items():  # Zliczanie występowania słowa po danych dwóch słowach poprzednich
    markov_corpus[x] = Counter(y)

for x in range(10):
    while True:
        kon = True
        pom = random.choice(list(markov_corpus.keys())).split()  # Losowy wybór początku zdania
        for x in pom:  # Zachowanie poprawności tworzonych zdań
            if re.match("[A-Z]", x[0]) is not None and (re.match(r"^[!.?]", x[len(x)-1])) is None:
                pass
            else:
                kon = False
        if kon == True:
            break
    wynik = pom

    # Tworzenie zdań nie krótszych niż 5 składowych oraz poprawne zakańczanie zdania
    # Zdanie budowane za pomocą prawdopodobieństwa występowania słowa następnego
    # po wystąpieniu 2 słów poprzedających
    while len(wynik) < 5 or re.match(r"[!.?]", pom[len(pom)-1]) is None:
        pom = random.choices(population=list(markov_corpus[wynik[-2] + " " + wynik[-1]].keys(), weights=list(markov_corpus[wynik[-2] + " " + wynik[-1]].values()), k=1)[0]
        wynik.append(pom)
    print(" ".join(wynik))
f.close()