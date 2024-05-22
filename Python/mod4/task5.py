from flask import Flask, request
import subprocess
import shlex

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def get_ps():
    args = request.args.getlist('arg')
    clean_args = [shlex.quote(arg) for arg in args] #Каждый аргумент обрамляется в кавычки с
    # помощью shlex.quote(), чтобы избежать проблем с метасимволами shell
    cmd = ['ps'] + clean_args # Формируется список аргументов команды ps
    result = subprocess.run(cmd, capture_output=True, text=True)#Запускается процесс ps с указанными аргументами.

    return f'<pre>{result.stdout}</pre>'


if __name__ == '__main__':
    app.run()
