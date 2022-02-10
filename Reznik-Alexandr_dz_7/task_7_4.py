import os

os.chdir(r'C:\PythonProjects\pythonProject\Python_tasks.git\Reznik-Alexandr_dz_7')

directory = 'some_data'
dict_compr = {10 ** x: 0 for x in range(1, 5)}
dict_compr[0] = 0
for files in os.walk(directory):
    item = files[2]
    if item:
        folder = files[0]
        for file in item:
            size = os.stat(os.path.join(folder, file)).st_size
            for key in dict_compr.keys():
                if size > key:
                    continue
                else:
                    dict_compr[key] += 1
                    break
result = {dict_compr: count for dict_compr, count in dict_compr.items() if count}
print(result)
# {10: 1, 1000: 10, 10000: 87}

