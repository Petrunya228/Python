import os
import re
from datetime import datetime, timedelta
import random
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def test_function():
    return f'привет мир!'


cars='Chevrolet, Renault, Ford, Lada'
@app.route('/cars')
def cars_function():
    return f'{cars}'


cats=['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route('/cats')
def cats_function():
    return random.choice(cats)



@app.route('/get_time/now')
def time_function():
    now=datetime.now().utcnow()
    return f'точное время- {now}'


@app.route('/get_time/future')
def future_function():
    current_time = datetime.now()
    time_after_hour = current_time + timedelta(hours=1)
    formatted_time = time_after_hour.strftime('%H:%M:%S')

    return f"Точное время через час будет {formatted_time}"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))#dirname-получениe директории файла,
# abspath-получиние абсолютного путя к файлу.
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')#join-объединяет путь BASE_DIR и
# имя файла "war_and_peace.txt" вместе
@app.route('/get_random_word')
def rand_function():
    with open(BOOK_FILE) as book:
        text = book.read()
        words = re.findall(r'\b\w+\b', text)#/b/w+/b-поиск всех "слов" в переменной text
        filtered_words = [word for word in words if word.isalnum()]#если слово является словом
        random_word = random.choice(filtered_words)
        return random_word



counter=0
@app.route('/counter')
def count_function():
    global counter#нужно чтобы увеличивать глобальную перменную на еденицу
    counter += 1
    return f"Страница открылась {counter} раз(а)"




if __name__=='__main__':
    app.run(port=5555, debug=True)
