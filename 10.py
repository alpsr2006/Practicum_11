print("Введите элементы первого списка через пробел:")
list1 = [int(num) for num in input().split()]

print("Введите элементы второго списка через пробел:")
list2 = [int(num) for num in input().split()]

print("Введите диапазон (два числа через пробел, например, 4 7):")
start_pos, end_pos = map(int, input().split())

start_index = start_pos - 1
end_index = end_pos

if 0 <= start_index < end_index <= len(list1):
    slice_to_move = list1[start_index:end_index]
    slice_to_move.reverse()

    list2.extend(slice_to_move)

    del list1[start_index:end_index]

    print(f"lst1 = {list1}")
    print(f"lst2 = {list2}")
else:
    print("Ошибка: указан некорректный диапазон.")