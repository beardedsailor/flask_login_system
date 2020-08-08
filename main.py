from flask import Flask, request, render_template, url_for, request, session, redirect
import pickle

app = Flask(__name__)

database = {'rahul': '1234', 'sahil': '5678'}

@app.route('/')
def hello_world():
    return render_template("login.html")




@app.route('/register', methods=['POST', 'GET'])

def register():
    if request.method == 'POST':
        name = request.form['usernam']
        passwd = request.form['passwor']
        if name in database:
            return render_template('signup.html', info='User exists. Use different username')
        else:
            database.update({name: passwd})
            return render_template('signup.html', info="Succesfully Registered")
    return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])

def login():
    if request.method == 'POST':
        name1 = request.form['username']
        pwd = request.form['password']
        if name1 not in database:
            return render_template('login.html', info='Invalid User.')
        else:
            if database[name1] != pwd:
                return render_template('login.html', info='Invalid Password')
            else:
                return render_template('home.html', name=name1)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
