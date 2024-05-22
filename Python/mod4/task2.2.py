from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError

app=Flask(__name__)

class NumberLength:
    def __init__(self, min, max, message=None):
        self.min=min
        self.max=max
        self.message=message
    def __call__(self, form: FlaskForm, field: Field):
        if len(str(field.data)) > self.min and len(str(field.data)) < self.max:
            error_message = self.message or f'Number stay in {min} and {max}'
            raise ValidationError(error_message)


class RegistrationForm(FlaskForm): # для каждого поля  внашем запросе мы создаём поле класса
    #обозначаем нижу, какие данные мы ждем из этих полей
    email=StringField(validators=[InputRequired(), Email()])
    phone=IntegerField(validators=[InputRequired(), NumberLength(5, 10, )])
    name=StringField(validators=[InputRequired()])
    address=StringField(validators=[InputRequired()])
    index=IntegerField(validators=[InputRequired()])
    comment=StringField()




@app.route('/registration', methods=['POST'])
def registration():
    form=RegistrationForm() # обьект формы

    if form.validate_on_submit(): #объект формы обращается к flask request, вытаскивает
        #нужные нам поля и сохраняет их
        email, phone=form.email.data, form.phone.data
    #form_data=request.get_data(as_text=True)

        return f"registrated user - {email} with phone- {phone}"

    return f"invalid input - {form.errors}", 400

if __name__=="__main__":
    app.config["WTF_CSRF_ENABLED"]=False# отключаем некоторые проверки безопасности
    app.run(debug=True)
