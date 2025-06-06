from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DEBUG, SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLAMCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    
with app.app_context():
    db.create_all()

    if not User.query.first():
        new_user = User(name='Maria', email='maria@gmail.com')
        db.session.add(new_user)
        db.session.commit()

@app.route('/')
def index():
    users = user.query.all()
    return '<br>' .join([f'Nome: {user.name}, Email: {user.email}' for user in users])

if __name__ == '__main__':
    app.run(debug=True)
