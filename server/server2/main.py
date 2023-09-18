
from flask import Flask
from app import create_app

app = Flask(__name__)
app = create_app()
app.config['SECRET_KEY'] = 'secret_key'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/fypserver'

if __name__ == "__main__":
    app.run(debug=True, port=8000)