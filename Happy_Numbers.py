def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

count = 0
num = 1
happy_numbers = []
while count < 8:
    if is_happy_number(num):
        happy_numbers.append(num)
        count += 1
    num += 1

print(happy_numbers)
