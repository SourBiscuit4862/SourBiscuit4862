from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

db = SQLAlchemy(app)
mail = Mail(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    verification_code = db.Column(db.String(6), nullable=True)
    verified = db.Column(db.Boolean, default=False)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

# Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.text

# Route for signing up
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    # Check if username or email already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'Username or email already exists'}), 400

    # Generate verification code
    verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Create user instance
    new_user = User(username=username, email=email, verification_code=verification_code)
    db.session.add(new_user)
    db.session.commit()

    # Send verification email
    send_verification_email(email, verification_code)

    return jsonify({'message': 'Verification code sent to your email'})

# Function to send verification email
def send_verification_email(email, verification_code):
    msg = Message('Verification Code', sender='your_email@example.com', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)

# Route for verifying email and completing signup
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    username = data.get('username')
    verification_code = data.get('verification_code')

    user = User.query.filter_by(username=username, verification_code=verification_code).first()
    if user:
        user.verified = True
        db.session.commit()
        return jsonify({'message': 'Email verified successfully'}), 200
    else:
        return jsonify({'message': 'Invalid verification code'}), 400

# Route for logging in
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    verification_code = data.get('verification_code')

    user = User.query.filter_by(username=username, verification_code=verification_code, verified=True).first()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username, verification code, or email not verified'}), 400

# Route for posting comments
@app.route('/comment', methods=['POST'])
def post_comment():
    data = request.get_json()
    username = data.get('username')
    text = data.get('text')

    user = User.query.filter_by(username=username).first()
    if user:
        new_comment = Comment(text=text, user_id=user.id)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({'message': 'Comment posted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

