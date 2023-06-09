import os
# import iris
from flask import Flask, render_template, request, url_for, redirect
import intersystems_iris.dbapi._DBAPI as iris



# ...
app = Flask(__name__)

env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)


def get_db_connection():
    host = app.config.get('HOST')
    port = 1972
    namespace = "USER"
    username = app.config.get('IRIS_USERNAME')
    password = app.config.get('IRIS_PASSWORD')
    

    conn = iris.connect(host, port, namespace, username, password)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()
    conn.close()
    secret_key = app.config.get("SECRET_KEY")

    # return f"The configured secret key is {secret_key}."
    return render_template('index.html', books=books)

# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (?, ?, ?, ?)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

