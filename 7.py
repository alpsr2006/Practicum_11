numbers = list(map(int, input().split()))

sum_even = 0
sum_odd = 0

for x in numbers:
    if x % 2 == 0:
        sum_even += x
    else:
        sum_odd += x

print(sum_even, sum_odd)