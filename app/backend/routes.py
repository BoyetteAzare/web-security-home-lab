
from flask import Blueprint, render_template, request, redirect, url_for, session
routes = Blueprint('routes',__name__)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        from app import mysql
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
            user = cursor.fetchone()
            cursor.close()

            if user:
                session['username'] = username
                return redirect(url_for('routes.dashboard'))
            else:
                return render_template('login.html', error='Invalid credentials')
        except:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')
@routes.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email= request.form['email']
        password = request.form['password']

        from app import mysql
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, password))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('routes.login'))
        except:
            return render_template('register.html', error='Registration failed. Please try again.')

    return render_template('register.html')


@routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@routes.route('/')
def index():
    return render_template('index.html')
@routes.route('/directory')
def directory():
    return render_template('directory.html')
@routes.route('/upload')
def upload():
    return render_template("upload.html")
@routes.route('/announcements')
def announcements():
    return render_template('announcements.html')
@routes.route('/admin')
def admin():
    return render_template('admin.html')
@routes.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes.login'))