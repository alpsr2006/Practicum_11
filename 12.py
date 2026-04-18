def count_hole_letters_in_word(word: str, hole_chars: set):
    """Вспомогательная функция: считает буквы
     с отверстиями в одном слове."""
    return sum(1 for char in word if char in hole_chars)

print("Введите строку из слов в нижнем регистре через пробел:")

text = input()

HOLE_CHARS = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}

holes_count = 0
no_holes_count = 0
for char in text:
    if 'a' <= char <= 'z':
        if char in HOLE_CHARS:
            holes_count += 1
        else:
            no_holes_count += 1

print(f"\nБукв с отверстиями: {holes_count}")
print(f"Букв без отверстий: {no_holes_count}")

words = text.split()
words_with_many_holes = [
    word for word in words
    if count_hole_letters_in_word(word, HOLE_CHARS) >= 2
]

print("\nСлова, имеющие две и более буквы с отверстиями:")
print(words_with_many_holes)