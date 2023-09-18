from flask import Flask, flash, redirect, render_template, request
from app.model import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def hello_world():
    return "Hello, MVC框架!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Users.query.filter_by(email=email).first()
        
        if user and user.password == password:
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html')
