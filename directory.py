import os

def print_directory_tree(startpath, exclude_dir):
    for root, dirs, files in os.walk(startpath):
        # Исключаем папку
        dirs[:] = [d for d in dirs if d != exclude_dir]

        # Вычисляем уровень вложенности
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')

        # Печать файлов в директории
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

if __name__ == '__main__':
    # Укажите директорию и папку для исключения
    project_dir = '.'  # Текущая директория
    exclude_dir = 'myenv'  # Папка для исключения

    print_directory_tree(project_dir, exclude_dir)
