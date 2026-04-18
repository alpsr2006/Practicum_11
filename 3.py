import re

sentence = input()

words = re.findall(r"[A-Za-zА-Яа-яЁё0-9]+", sentence)

print(words)