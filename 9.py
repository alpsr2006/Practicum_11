import re

words = []
# Позиция слова в тексте (для сохранения порядка появления)
position = 0

while True:
    line = input()
    if line == "":
        break

    tokens = re.findall(r"[A-Za-zА-Яа-яЁё0-9]+", line.lower())

    for token in tokens:
        words.append(token)
        position += 1

# Хранит частоту встречаемости каждого слова
freq = {}
first_pos = {}

for idx, word in enumerate(words):
    if word not in freq:
        freq[word] = 0
        first_pos[word] = idx
    freq[word] += 1

# Сортировка: сначала по частоте (убывание), затем по первому появлению
sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], first_pos[w]))

for word in sorted_words:
    print(word)