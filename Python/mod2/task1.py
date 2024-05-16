def get_summary_rss(file_path):
    total_memory=0

    with open(file_path, 'r') as file:
        lines=file.readlines()[1:]
        for line in lines:
            columns=line.split()
            memory_in_bytes=int(columns[5])#извлекаем 6 элемент из списка и преобразуем его в число
            # (должна содержаться информация о памяти в байтах
            total_memory+=memory_in_bytes

    def convert_bytes(memory_bytes):
        units=['Б','Кб','Мб','Гб','Тб']
        unit_index=0
        while memory_bytes >=1024 and unit_index<len(units):
            memory_bytes/=1024
            unit_index+=1
        return f"{memory_bytes:.0f}{units[unit_index]}"
    return convert_bytes(total_memory)

file_path='output_file.txt'
print(get_summary_rss(file_path))
