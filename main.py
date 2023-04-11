from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
import os
from db_handler import DatabaseHandler
import dotenv
from jose import jwt
# add unix epoch time
from datetime import datetime

STATIC_FOLDER = 'templates/assets'
UPLOAD_FOLDER = 'files'


app=Flask(__name__, static_folder=STATIC_FOLDER) #initiating flask object
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
            return redirect(url_for('login'))

    return wrapper

@app.route('/')
@login_required
def index():
    db = DatabaseHandler()

    #decoding and checking token
    token = session['token']
    username = get_username_from_token(token)
    if username is None:
        return redirect(url_for('login'))

    # Getting the tags filters
    post_sort = request.args.get('post_category')
    if post_sort is None:
        post_sort = 'top'
    post_time = request.args.get('post_time')
    if post_time is None:
        post_time = 'all'

    # Getting the posts
    
    print(post_sort, post_time)
    tags = db.get_tags(post_sort, post_time)

    table_sort = request.args.get('table_category')
    if table_sort is None:
        table_sort = 'top'
    table_time = request.args.get('table_time')
    if table_time is None:
        table_time = 'all'

    print(table_sort, table_time)

    posts = db.get_posts(table_sort, table_time)

    db.close()



    return render_template('index.html', username=username, tags=tags, posts=posts)

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
        return redirect(url_for('login'))
    db = DatabaseHandler()
    if db.get_user_by_username(username) is None:
        db.add_user(username, password)
        db.close()
        flash(('User created successfully', 'success'))
        return redirect('/login')
    else:
        flash(('Username already exists', 'danger'))
        return redirect(url_for('login'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        title = request.form['title']
        tags = request.form['tags']
        tags = tags.replace(' ', '')
        content = request.form['content']
        try:
            token = session['token']
        except:
            return redirect(url_for('login'))
        username = get_username_from_token(token)
        if username is None:
            flash(('You need to login first', 'danger'))
            return redirect(url_for('login'))
        file = request.files['file']
        filename = ''
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        db = DatabaseHandler()

        #def add_post(self, title, content, tags, username, filename):
        db.add_post(title, content, tags, username, filename)
        db.close()
        flash(('Post added successfully', 'success'))
        return redirect('/')

@app.route('/search', methods=['GET'])
def search():
    search = request.args.get('search')
    if search is None:
        search = ''
        print("Searched nothing")

    sort = request.args.get('sort')
    if sort is None:
        sort = 'top'
    time = request.args.get('time')
    if time is None:
        time = 'all'

    quantity = request.args.get('quantity')
    if quantity is None:
        quantity = 20
    #check if quantity is a number
    try:
        quantity = int(quantity)
    except:
        quantity = 20


    
    db = DatabaseHandler()
    posts = db.search_posts(search, sort, time, quantity)
    db.close()
    print("SEARCH: ", search)
    for post in posts:
        print(post)
    return render_template('search.html', search=search, posts=posts)

@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    db = DatabaseHandler()
    user_id = db.get_user_by_username(username).id
    posts = db.get_posts_by_user_id(user_id)
    db.close()
    return render_template('user.html', posts=posts, username=username)

@app.route('/post/<post_id>')
def post(post_id):
    db = DatabaseHandler()
    post, tags = db.get_post_by_id(post_id)
    username = post.user.username
    #checks if user role is admin or post owner
    role = db.get_user_by_username(username).role
    db.close()
    try:
        token = session['token']
    except:
        return redirect(url_for('login'))
    username = get_username_from_token(token)
    if username is None:
        return redirect(url_for('login'))
    #checks if user role is admin or post owner
    role = db.get_user_by_username(username).role
    if username == post.user.username or role == 'admin':
        return render_template('post.html', post=post, username = username, tags=tags, admin=True)
    else:
        return render_template('post.html', post=post, username = username, tags=tags)

@app.route('/file/<post_id>')
def file(post_id):
    db = DatabaseHandler()
    post = db.get_post_by_id(post_id)
    print(post[0].file_names)
    db.close()
    return send_from_directory(app.config['UPLOAD_FOLDER'], post[0].file_names)

@app.route('/users')
def users():
    db = DatabaseHandler()
    users = db.get_users()
    db.close()
    return render_template('users.html', users=users)

@app.route('/admin/delete/<post_id>')
def delete_post(post_id):
    try:
        token = session['token']
    except:
        return redirect(url_for('login'))
    username = get_username_from_token(token)
    if username is None:
        return redirect(url_for('login'))
    db = DatabaseHandler()
    role = db.get_user_by_username(username).role
    if role != 'admin':
        return redirect(url_for('login'))
    db.delete_post(post_id)
    db.close()
    flash(('Post deleted successfully', 'success'))
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

@app.route('/vote/<post_id>')
def upvote(post_id):
    try:
        token = session['token']
    except:
        return redirect(url_for('login'))
    username = get_username_from_token(token)
    if username is None:
        return redirect(url_for('login'))
    db = DatabaseHandler()
    task = request.args.get('task')
    db.vote_post(post_id, task)
    print(task)
    db.close()
    return redirect('/post/' + post_id)



if __name__ == '__main__':
    app.run(debug=True, port=80)