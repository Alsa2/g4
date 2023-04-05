from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from db_handler import DatabaseHandler
import dotenv
from jose import jwt
# add unix epoch time
from datetime import datetime

STATIC_FOLDER = 'templates/assets'


app=Flask(__name__, static_folder=STATIC_FOLDER) #initiating flask object

dotenv.load_dotenv()
token_encryption_key = os.getenv('TOKEN_ENCRYPTION_KEY')
#token_encryption_key = 'secret'

secret_key = os.urandom(24)
app.secret_key = secret_key


def create_token(username, token_duration): #token = encoded(username, datetime) token_duration in minutes
    # Unix Epoch time
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    ttl = token_duration * 60 + unix_timestamp
    token  = jwt.encode({'username': username, 'datetime': unix_timestamp}, token_encryption_key, algorithm='HS256')
    return token

def get_username_from_token(token): #get username from token
    print(token)
    try: 
        decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
    except:
        return None
    return decoded_token['username']

def check_token(token): #check if token is valid and not expired
    try:
        decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
        unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
        if decoded_token['datetime'] < unix_timestamp:
            return False
        else:
            return True
    except:
        return False



def login_required(f):
    def wrapper(*args, **kwargs):
        if 'token' in session:
            return f(*args, **kwargs)
        else:
            flash(('You need to login first', 'danger'))
            return render_template('login.html', )

    return wrapper

@app.route('/')
@login_required
def index():
    #decoding token
    token = session['token']
    username = get_username_from_token(token)
    if username is None:
        return redirect(url_for('login'))
    db = DatabaseHandler()
    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        remember_me = request.form.get('rememberMe') == 'on' # To implement remember me
        db = DatabaseHandler()
        if db.login(username, password):
            token = create_token(username, 60)
            session['token'] = token
            db.close()
            return redirect('/')
        else:
            db.close()
            message = ('Wrong username or password!', 'danger')
            flash(message)
            return redirect(url_for('login'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['newUsername']
    password = request.form['newPassword']
    password_confirmation = request.form['confirmPassword']
    if password != password_confirmation:
        msg =('Passwords do not match', 'danger')
        flash(msg)
        return redirect(url_for('register'))
    db = DatabaseHandler()
    if db.get_user_by_username(username) is None:
        db.add_user(username, password)
        db.close()
        return redirect('/login')
    else:
        flash('Username already exists')
        return redirect(url_for('register'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        title = request.form['title']
        tags = request.form['tags']
        content = request.form['content']
        username = get_username_from_token(session['token'])
        db = DatabaseHandler()
        db.add_post(title, tags, content, username)
        db.close()
        return redirect('/')

@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    db = DatabaseHandler()
    user_id = db.get_user_by_username(username).id
    posts = db.get_posts_by_user_id(user_id)
    db.close()
    return render_template('user.html', posts=posts, username=username)

@app.route('/users')
def users():
    db = DatabaseHandler()
    users = db.get_users()
    db.close()
    print(users)
    return render_template('users.html', users=users)

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

@app.route('/test')
def test():
    render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)