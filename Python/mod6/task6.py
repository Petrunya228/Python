from flask import Flask, render_template, redirect, url_for
from werkzeug.routing import BuildError

app = Flask(__name__)

# Здесь определяются все ваши маршруты (endpoints)
@app.route('/')
def index():
    return 'Главная страница'

@app.route('/about')
def about():
    return 'О нас'

# Декоратор для обработки ошибки 404
@app.errorhandler(404)
def page_not_found(error):
    available_pages = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods:
            available_pages.append(rule.endpoint)
    return render_template('404.html', available_pages=available_pages), 404

# Обработчик для перехода на другие страницы
@app.route('/<page>')
def redirect_to_page(page):
    try:
        return redirect(url_for(page))
    except BuildError:
        return page_not_found(404)

if __name__ == '__main__':
    app.run(debug=True)
