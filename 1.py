initial_list = []
for _ in range(10):
    number = int(input())
    initial_list.append(number)

new_list = [
    initial_list[i] + initial_list[i + 1] for i in range(8)
]

print(f"Новый список: {new_list}")