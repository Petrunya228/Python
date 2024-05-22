import shlex
import subprocess
from typing import Tuple

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED']=False

class CodeForm(FlaskForm):
    code= StringField(validators=[InputRequired()])
    timeout=IntegerField(default=10)

    def runCode(code: str, timeout: int) -> Tuple[str, str, bool]:
        command=f'python3 -c "{code}"'
        command=shlex.split(command)
        process=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        was_kill=False
        try:
            outs, errs= process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            outs, errs=process.communicate()
            was_kill=True
        return outs.decode(), errs.decode(), was_kill

@app.route('/run_code', methods=['POST'])
def run_code():
    form=CodeForm()
    if form.validate_on_submit():
        code=form.code.data
        timeout=form.timeout.data
        stdout, stderr, killed= run_code(code=code, timeout=timeout)
        return f'stdout- {stdout}, stderr- {stderr}, kill- {killed}'
    return f'bad - {form.errors}'

if __name__=='__main__':
    app.run(debug=True)