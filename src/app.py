from flask import Flask, render_template

app = Flask(__name__)

#INDEX
@app.route('/', methods=['GET'])
def index():



    return render_template('index.html')

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