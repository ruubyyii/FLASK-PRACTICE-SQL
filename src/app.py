from flask import Flask, render_template, flash, redirect, url_for, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

mysql = MySQL(app)

#INDEX
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM products')
        products = cur.fetchall()

        return render_template('index.html', products=products)
    
    if request.method == 'POST':
        flash('Tienes que registrarte antes de añadir un producto a favoritos.')
        return redirect(url_for('index'))

#REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'GET':

        return render_template('register.html')

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        print(name, email, password)

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users VALUES(NULL, %s, %s, %s)', (name, email, password))
        mysql.connection.commit()

        return redirect(url_for('login'))

#LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':

        return render_template('login.html')

    if request.method == 'POST':

        name = request.form.get('name')
        password = request.form.get('password')

        cur = mysql.connection.cursor()
        cur.execute('SELECT id, name, password FROM users WHERE name = %s AND password = %s', (name, password))
        user = cur.fetchone()
        print(user)
        if user:
            print('SOY UN PEDAZO DE POLLA GORDA😋')

            return redirect(url_for('perfil', user_id=user[0]))

    return 'TENGO EL PENE PEQUENITO | User: {}'.format(user)

@app.route('/perfil/<int:user_id>')
def perfil(user_id):

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cur.fetchone()
    print(user)
    return render_template('perfil.html', user=user)

#USERS
@app.route('/users', methods=['GET'])
def users():

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()