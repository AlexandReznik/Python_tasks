import os


def create_dirs(base_folder, daughter_folder_1, daughter_folder_2, daughter_folder_4, daughter_folder_5):
    dir_path = os.path.join(base_folder, daughter_folder_1)
    dir_path_2 = os.path.join(base_folder, daughter_folder_2)
    dir_path_3 = os.path.join(base_folder, daughter_folder_4)
    dir_path_4 = os.path.join(base_folder, daughter_folder_5)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        os.makedirs(dir_path_2)
        os.makedirs(dir_path_3)
        os.makedirs(dir_path_4)


create_dirs('my_project_1', 'settings', 'mainapp', 'authapp', 'adminapp')
