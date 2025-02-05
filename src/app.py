from flask import Flask, render_template, flash, redirect, url_for, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
# Inicio MySQL en mi applicacion.
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

    return render_template('register.html')

#LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')

#USERS
@app.route('/users', methods=['GET'])
def users():

    return render_template('users.html')



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()