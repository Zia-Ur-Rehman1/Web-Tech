from flask import Flask
from flask import render_template
from flask import session, request
from flask import redirect, url_for
from flask import flash
import sqlite3 as sql

import json

# Creating an object  and passing modul name
app = Flask(__name__)
app.secret_key = b"4567[]8'\@##$%&^@9iuhDFDD()*@(*Ff/.,.\z,.213te[][dwp"

user_email = 'admin@zia'
user_pass = 'admin'

# Authentication
@app.route('/', methods=['GET', 'POST'])
def index():
    if(session.get('username')):
        flash('Your have to logout first', 'info')
        return redirect(url_for('home'))

    if(request.method == 'POST'):
        if not request.form['email'] or not request.form['password']:
            flash('Email or Password cannot be empty', 'warning')

        # request.form will show you the input of form
        elif request.form['email'] == user_email and request.form['password'] == user_pass:

            session['username'] = request.form['email']
            return redirect(url_for('home'))
        else:
            flash('Your email or password is incorrect', 'warning')
            return redirect(url_for('index'))
    else:
        return render_template('login.html')

# Homepage
@app.route('/home')
def home():
    if(session.get('username')):
        return render_template('home.html')
    else:
        return redirect(url_for('index'))

#Students data with db
@app.route('/student')
def show_student():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from students")
   
    rows = cur.fetchall(); 
    if(rows==None):
        flash("Nothing to Display")
    return render_template("student.html",rows = rows)

@app.route('/rec', methods=['POST','GET'])
def add_rec():
    if request.method == 'POST':
        print("Zia")
        try:
            name = request.form['name']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            
            with sql.connect("database.db") as con:
                
                cur = con.cursor()
                cur.execute("INSERT INTO students (username,addr,city,pin) VALUES (?,?,?,?)",(name,addr,city,pin) )
                con.commit()
                msg = "Record successfully added"
        except:
            msg = "error in insert operation"
      
        finally:
            con.close()
            return render_template("result.html",msg = msg)
            

    

@app.route('/remove/<user_id>')
def remove(user_id):
    try:
        with sql.connect("database.db") as con:
            cur=con.cursor()
            cur.execute("DELETE FROM students WHERE id = ?",(user_id,))
            con.commit()
    except:
        msg = "error in insert operation"
    finally:
        con.close()
        return show_student()




@app.route('/logout')
def logout():
    if(session.pop('username')):
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


    # con_db()
# def con_db():
#     try:
#         conn = sqlite3.connect('database.db')
#         print ("Opened database successfully")
#         conn.execute('CREATE TABLE students ( id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,addr TEXT NOT NULL, city TEXT NOT NULL, pin TEXT NOT NULL)')
#         print ("Table created successfully")
#         conn.close()
#     except:
#         print("Some Error Occured")
