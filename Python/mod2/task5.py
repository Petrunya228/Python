from flask import Flask

app=Flask(__name__)

@app.route("/max_number/<path:number>")
def even(number):
    new_num=number.split('/')
    new_num = [int(num) for num in new_num if num.isdigit()]
    if new_num:
        max_num = max(new_num)
        return f"Максимальное число: {max_num}"

if __name__=="__main__":
    app.run(debug=True)
