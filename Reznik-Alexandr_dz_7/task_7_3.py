import os
import shutil

try:
    new_dir_path = os.path.join('my_project', 'templates')
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)

    folder = r'C:\PythonProjects\pythonProject\Python_tasks.git\Reznik-Alexandr_dz_7\my_project\mainapp\templates\mainapp'
    folder_2 = r'C:\PythonProjects\pythonProject\Python_tasks.git\Reznik-Alexandr_dz_7\my_project\authapp\templates\authapp'
    folder_paste_2 = r'C:\PythonProjects\pythonProject\Python_tasks.git\Reznik-Alexandr_dz_7\my_project\templates'

    path_app = r'C:\PythonProjects\pythonProject\Python_tasks.git\Reznik-Alexandr_dz_7\my_project\templates\mainapp'
    path_app_2 = r'C:\PythonProjects\pythonProject\Python_tasks.git\Reznik-Alexandr_dz_7\my_project\templates\authapp'
    if not os.path.exists(path_app) and not os.path.exists(path_app_2):
        shutil.move(folder, folder_paste_2)
        shutil.move(folder_2, folder_paste_2)
except (FileExistsError, FileNotFoundError) as e:
    print(f'Ошибка: {e}')
except Exception as er:
    print(f'Глобальная ошибка: {er}')





