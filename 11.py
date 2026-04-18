numbers = list(map(int, input().split()))
command = input().strip()

direction = command[0].upper()
shift = int(command[1:])

if numbers:
    # Нормализуем сдвиг, чтобы не делать лишних оборотов
    shift %= len(numbers)

if direction == "R":
    result = numbers[-shift:] + numbers[:-shift]
elif direction == "L":
    result = numbers[shift:] + numbers[:shift]
else:
    result = numbers

print(result)