import os
from flask import Flask, request

app=Flask(__name__)

@app.route('/preview/int:SIZE/path:RELATIVE_PATH')
def preview(SIZE, RELATIVE_PATH):
    abs_path=os.path.abspath(RELATIVE_PATH)
    result_text=""
    try:
        with open(abs_path, 'r') as file:
            result_text=file.read(SIZE)
    except FileNotFoundError:
        return "нет"
    result_size=len(result_text)

    return f"<b>{abs_path}</b> {result_size}<br>{result_text}"

if __name__=="__main__":
    app.run(debug=True)
