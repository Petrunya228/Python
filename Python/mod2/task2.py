import sys

def get_mean_size(data):
    lines=data.splitlines()[1:] # Пропускаем первую строку (заголовок)
    total_size = 0
    num_files = 0
    for line in lines:
        columns=line.split()
        if len(columns) > 4:  # Проверяем, что строка содержит информацию о размере файла
            file_size=int(columns[4])#берем размер файла из пятого столбца
            total_size += file_size
            num_files += 1
    if num_files == 0:
        return "нет"
    mean_size = total_size / num_files
    return mean_size

data = sys.stdin.read()
print(get_mean_size(data))
