import re

sentence = input()

words = re.findall(r"[A-Za-zА-Яа-яЁё0-9]+", sentence)

unique_words = []
seen = set()

for word in words:
    key = word.lower()
    if key not in seen:
        unique_words.append(key)
        seen.add(key)

print(unique_words)