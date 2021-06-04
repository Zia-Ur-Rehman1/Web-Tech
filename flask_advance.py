from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import redirect,url_for
from flask.helpers import flash
# Creating an object  and passing modul name
app = Flask(__name__)
app.secret_key=b"4567[]8'\@##$%&^@9iuhDFDD()*@(*Ff/.,.\z,.213te[][dwp"


@app.route('/',methods=['GET','POST'])
def index():
    if(request.method=='POST'):
        # request.form will show you the input of form
        email=request.form['email']
        password=request.form['password']
        if not email or not password:
            flash("Your email or password is incorrect")
            return redirect(url_for('index'))

        session['username']=email
        return redirect(url_for('home'))
    return render_template('login.html')
@app.route('/home')
def home():
    if(session.get('username')):
        return render_template('home.html')
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if(session.pop('username')):
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
