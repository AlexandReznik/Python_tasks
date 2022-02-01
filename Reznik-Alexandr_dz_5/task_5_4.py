def get_numbers(list_numbers: list):
    result = []
    for num in range(1, len(list_numbers)):
        if list_numbers[num] > list_numbers[num - 1]:
            result.append(list_numbers[num])
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(get_numbers(src))


def get_numbers_2(numbers: list):
    num_gen = (numbers[num] for num in range(1, len(numbers))
               if numbers[num] > numbers[num - 1])
    return num_gen


list_num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers_2(list_num))
