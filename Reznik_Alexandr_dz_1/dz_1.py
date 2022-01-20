# 1
time = int(input('Enter seconds:'))
day = time // 24 // 3600
hours = time // 3600 - (day*24)
min = time // 60 - (day*24*60) - hours * 60
sec = time - (min*60) - (hours*3600)
print(f'{day} дн {hours} час {min} мин {sec} сек')


# 2
my_list = [i**3 for i in range(1, 1001, 2)]
my_list_2 = []
#a
for i in my_list:
    if i % 7 == 0:
        my_list_2.append(i)
print('a)', my_list_2)
print('Sum of list:', sum(my_list_2))
#b
my_list_3 = [n + 17 for n in my_list_2]
my_list_4 = []
print('b)', my_list_3)
print('Sum of elements:', sum(my_list_3))

for i in my_list_3:
    if i % 7 == 0:
        my_list_4.append(i)

print(sum(my_list_4))

# 3
"""
print('Third task:')
for n in range(1, 101):
    if :
        print('процент')
"""





