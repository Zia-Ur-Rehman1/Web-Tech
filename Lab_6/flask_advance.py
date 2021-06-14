from flask import Flask,render_template,session,request,redirect,url_for,flash
import json

from flask.json import loads
# Creating an object  and passing modul name
app = Flask(__name__)
app.secret_key=b"4567[]8'\@##$%&^@9iuhDFDD()*@(*Ff/.,.\z,.213te[][dwp"
API_DATA = '{"data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://reqres.in/img/faces/1-image.jpg"},{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},{"id":3,"email":"emma.wong@reqres.in","first_name":"Emma","last_name":"Wong","avatar":"https://reqres.in/img/faces/3-image.jpg"},{"id":4,"email":"eve.holt@reqres.in","first_name":"Eve","last_name":"Holt","avatar":"https://reqres.in/img/faces/4-image.jpg"},{"id":5,"email":"charles.morris@reqres.in","first_name":"Charles","last_name":"Morris","avatar":"https://reqres.in/img/faces/5-image.jpg"},{"id":6,"email":"tracey.ramos@reqres.in","first_name":"Tracey","last_name":"Ramos","avatar":"https://reqres.in/img/faces/6-image.jpg"}]}'

user_email='zia2018@namal.edu.pk'
user_pass='mr1540724'



    
@app.route('/',methods=['GET','POST'])
def index():
    if(session.get('username')):
        flash(u'Your have to logout first','info')
        return redirect(url_for('home'))
    
    if(request.method=='POST'):
        if not request.form['email'] or not request.form['password']:
            flash(u'Email or Password cannot be empty','warning')

        # request.form will show you the input of form
        elif  request.form['email']==user_email and request.form['password']== user_pass:

            session['username']=request.form['email']
            return redirect(url_for('home'))      
        else:
            flash(u'Your email or password is incorrect','warning')
            return redirect(url_for('index'))
    return render_template('login.html')



@app.route('/home')
def home():
    if(session.get('username')):
        return render_template('home.html',data=json.loads(API_DATA),name=session.get('username'))
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    if(session.pop('username')):
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
