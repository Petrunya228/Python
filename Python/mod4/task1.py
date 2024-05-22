from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange

app=Flask(__name__)

class RegistrationForm(FlaskForm): # для каждого поля  внашем запросе мы создаём поле класса
    #обозначаем нижу, какие данные мы ждем из этих полей
    email=StringField(validators=[InputRequired(), Email()])
    phone=IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
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
