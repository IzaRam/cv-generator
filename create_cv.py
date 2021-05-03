from flask import Flask, render_template
from forms import RegisterCv

app = Flask(__name__)
app.config['SECRET_KEY'] = '19f4c4b47c8e726dec271f44'


@app.route('/new_cv', methods=['GET', 'POST'])
def create_cv():
    cv_form = RegisterCv()
    if cv_form.is_submitted():
        print(cv_form.name.data)
        print(cv_form.email.data)
        print(cv_form.phone.data)
    return render_template('cv_form.html', form=cv_form)


if __name__ == '__main__':
    app.run(debug=True)
