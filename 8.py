def sort_chars(text):
    """
    Преобразует строку в список символов, сортирует его,
    затем собирает обратно в строку и возвращает результат.
    """
    chars = list(text)
    chars.sort()
    return "".join(chars)


s = input()
print(sort_chars(s))