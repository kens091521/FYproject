from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # 更換為您自己的密鑰
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/fypserver'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User {self.username}>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # 使用提供的電子郵件查詢符合條件的用戶
        user = Users.query.filter_by(email=email).first()
        
        if user and user.password == password:
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True, port=8000)