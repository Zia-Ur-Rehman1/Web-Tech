from flask import Flask
from flask import render_template
from flask import request
# Creating an object  and passing modul name
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template ('index.html')


@app.route('/home')
def home():
    return ("Home")

# <int:user_id> u can define datatype with it also
@app.route('/user/<user_id>')
def user(user_id):
    return f"User id {user_id}"

@app.route('/link')
def link():
    return '<a href="user/1122">User</a>'

@app.route('/user_name/<username>')
def user_name(username):
    # (name) this will used to access data in html
    return render_template('index.html',name=username)

if __name__ == '__main__':
    app.run(debug=True)
