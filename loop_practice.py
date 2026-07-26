# Дан список чисел - удали из него все чётные числа, не сломав перебор.
numbers = [23, 12, 8, 15, 42, 9, 7, 30, 19,20, 4, 51, 12, 37, 26, 9, 44, 17]

for num in numbers.copy():
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)

# Дан список строк - удали все строки короче 3 символов.

words = ["a", "hi", "python", "development", "go", "elephant", "7", "ok", "programming", "up", "computer"]

long_words = []

for word in words:
    if len(word) >= 3:
        long_words.append(word)

print(long_words)

