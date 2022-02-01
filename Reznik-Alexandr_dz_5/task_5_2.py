def odd_nums(number):
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    nums_gen = (num for num in range(1, number + 1, 2))
    return nums_gen


n = 17
generation = odd_nums(n)
for _ in range(1, n+1, 2):
    print(next(generation))
