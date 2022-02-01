def get_uniq_numbers(nums: list):
    result_list = []
    for num in nums:
        if nums.count(num) == 1:
            result_list.append(num)
    return result_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(get_uniq_numbers(src))
