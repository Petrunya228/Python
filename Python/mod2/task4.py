from flask import Flask
from datetime import datetime

app=Flask(__name__)

def get_weekdays():
    weekdays={
        0: "понедельник",
        1: "вторник",
        2: "среда",
        3: "четверг",
        4: "пятница",
        5: "суббота",
        6: "воскресенье",
    }
    return weekdays[datetime.today().weekday()]

@app.route('/hello/<username>')
def hello(username) -> str:
    return f"<h1>hello, {username} хорошей {get_weekdays()}</h1>"

if __name__=="__main__":
    app.run(debug=True)
