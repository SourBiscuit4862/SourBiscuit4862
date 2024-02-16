from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy user database
users = {
    'user1': {
        'username': 'user1',
        'password': 'password1'
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            # Log in user
            return 'Logged in successfully'
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username is already taken
        if username in users:
            return 'Username already exists'
        # Add new user to database
        users[username] = {'username': username, 'password': password}
        return 'Signed up successfully'
    return render_template('signup.html')

@app.route('/save_comment', methods=['POST'])
def save_comment():
    comment = request.form.get('comment')
    with open('save.data.txt', 'a') as file:
        file.write(comment + '\n')
    return 'Comment saved successfully'

@app.route('/upload_video', methods=['POST'])
def upload_video():
    # Handle video upload logic here
    return 'Video uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
