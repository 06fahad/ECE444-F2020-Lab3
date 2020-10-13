from flask import Flask, render_template, session, flash
from flask_bootstrap import Bootstrap
from datetime import date, datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField 
from wtforms.validators import Required, Email
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'never_guess_this'
bootstrap = Bootstrap(app)



class RegForm(Form):
    name = StringField('What is your name?', validators = [Required()])
    email = StringField('What is your UofT Email address?', validators = [Required(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['POST', 'GET'])
def index():
    form = RegForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            old_name = session.get('name')
            old_email = session.get('email')

            if old_name is not None and old_name != form.name.data:
                flash('Looks like you have changed your name!')
            else:
                session['name'] = form.name.data

            if old_email is not None and old_email != form.email.data:
                flash('Looks like you have changed your email!')
            else:
                session['email'] = form.email.data

            if(form.email.data.endswith('@mail.utoronto.ca')):
                corr_email = True
            else:
                corr_email = False
            
            return render_template('form.html', form=form, name=form.name.data, email=form.email.data, corr_email=corr_email)     
        else:
            return render_template('form.html', form=form)
    else:
        return render_template('form.html', form=form)

@app.route('/user/<name>')
def user(name):
    # datetime object containing current date and time
    now = datetime.now()
    return render_template('page.html', name=name, now=now)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')