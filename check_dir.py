import os

# Объем всех файлов с учетом вложенных директорий


def size_count(path):
    os.chdir(path)
    size_sum = 0
    for obj in os.listdir(path):
        if os.path.isfile(obj):
            size_sum += os.path.getsize(obj)
        elif os.path.isdir(obj):
            for inner_obj in os.listdir(obj):
                if os.path.isfile(inner_obj):
                    size_sum += os.path.getsize(inner_obj)
    return size_sum

# Поиск в именах файлов


def name_search(path, search_string):
    os.chdir(path)
    count = 0
    for obj in os.listdir(path):
        if os.path.isfile(obj) and search_string in obj:
            count += 1
            print(obj)
    return count

