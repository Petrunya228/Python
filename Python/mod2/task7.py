from flask import Flask, jsonify #удобное форматирование овтетов в формате json

app= Flask(__name__)
storage={}

@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    year= int(date[:4])
    month=int(date[4:6])
    day=int(date[6:])

    #setdefault- добавление элемента в слварь с указанным ключом и значением
    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0) #добавляем в наш пустой словарь значение по умолчанию (пустые)
    storage[year][month][day]+=number #к каждому из значений добавляем наши затраты

    return f'трата - {number}'

@app.route('/calculate/<int:year>')
def calculate_year(year):
    if year in storage:
        total_spent=0
        for month in storage[year]:
            for day in storage[year][month]:
                total_spent+=storage[year][month][day] #переби раем каждый день каждого месяц данного года
        return jsonify({'total': total_spent})# возвращаеём всё в формате json
    else:
        return 'не та дата'

@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    if year in storage and month in storage[year]:# есть ли в словаре запись для указанного месяца и года
        total_spent=sum(storage[year][month].values())# скалдываем все расходы за месяц
        return jsonify({'total': total_spent})
    else:
        return ('не та дата')

if __name__=="__main__":
    app.run(debug=True)
