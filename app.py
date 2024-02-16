from flask import Flask, request, jsonify
import random
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Temporary storage for user data
users = {}

# Email configuration (replace with your own SMTP server details)
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USERNAME = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

# Function to generate a random verification code
def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))

# Route for signing up
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    
    # Generate verification code
    verification_code = generate_verification_code()
    
    # Store user data with verification code
    users[username] = {
        'email': email,
        'verification_code': verification_code
    }

    # Send verification email
    send_verification_email(email, verification_code)

    return jsonify({'message': 'Verification code sent to your email'})

# Function to send verification email
def send_verification_email(email, verification_code):
    msg = MIMEText(f'Your verification code is: {verification_code}')
    msg['Subject'] = 'Verification Code'
    msg['From'] = EMAIL_USERNAME
    msg['To'] = email

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, [email], msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
