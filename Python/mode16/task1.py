import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')

# Создание курсора
cur = conn.cursor()

# Создание таблицы актеров
cur.execute('''
    CREATE TABLE IF NOT EXISTS actors (
        act_id INTEGER PRIMARY KEY,
        act_first_name varchar(50),
        act_last_name varchar(50),
        act_gender varchar(1)
    )
''')

# Создание таблицы фильмов
cur.execute('''
    CREATE TABLE IF NOT EXISTS movie (
        mov_id INTEGER PRIMARY KEY,
        mov_title varchar(50)
    )
''')

# Создание таблицы режиссеров
cur.execute('''
    CREATE TABLE IF NOT EXISTS director (
        dir_id INTEGER PRIMARY KEY,
        dir_first_name varchar(50),
        dir_last_name varchar(50) 
    )
''')

# Создание таблицы актерского состава фильмов
cur.execute('''
    CREATE TABLE IF NOT EXISTS movie_cast (
        act_id INTEGER,
        mov_id INTEGER,
        role varchar(50),
        FOREIGN KEY (act_id) REFERENCES actors(act_id),
        FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
    )
''')

# Создание таблицы оскаров
cur.execute('''
    CREATE TABLE IF NOT EXISTS oscar_awarded (
        award_id INTEGER PRIMARY KEY,
        mov_id INTEGER,
        FOREIGN KEY (mov_id) REFERENCES movie(mov_id)
    )
''')

# Создание таблицы направления фильмов
cur.execute('''
    CREATE TABLE IF NOT EXISTS movie_direction (
        dir_id INTEGER,
        mov_id INTEGER,
        FOREIGN KEY (dir_id) REFERENCES director(dir_id)
    )
''')

# Подтверждение изменений
conn.commit()

# Закрытие соединения с базой данных
conn.close()

# Вывод сообщения о завершении
print('База данных и таблица успешно созданы!')
