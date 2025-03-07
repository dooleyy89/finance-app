# 'request' handles incoming HTTP requests and extract data from them
# 'jsonify' used to send JSON responses from Flask endpoints
from flask import Flask, request, jsonify
from flask_mysql import MySQL

# library for securely hashing passwords, ensuring that if someone gets
# access to database they can't easily retrieve user passwords
from flask_bcrypt import Bcrypt

# JWTMANAGER extension helps with creating, verifying, handling JWT tokens
# create_a_t creates JWT token after successful login
# jwt_requred decorator used to protect routes so only users with valid JWT tokens can access
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# create flask instance
app = Flask(__name__)

"""
# mysql configurations (SQLALCHEMY)
#   add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:ddoo4644@localhost:3306/finance_user_db'
#   for better run time
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#   secret key for encoding JWT
app.config['SECRET_KEY'] = ''
"""

# MySQL config
app.secret_key = 'igotdakeysdakeys'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =
app.config['MYSQL_DB'] = 'finance_user_db'


# initialize extensions, allowing flask to interact with mySQL db, app to securely hash passwords and check hashed passwords, and JWTManager to handle creation, parsing, and verification of JWT tokens
mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() # reads incoming JSON data in request body, converts to python dictionary
    email = data.get('email') # extracts email and password values from incoming request data
    password = data.get('password')
    
    # checks if either field is missing from request. if so:
    # - returns JSON response w/ err msg and 400 status code (bad request)
    if not email or not password:
        return jsonify({"msg": "Email and password are required"}), 400

    # hashes user's pswd using bcrypt, hashed pass is stored in database instead of plain-text pswd
    hashed_pswd = bcrypt.generate_password_hash(password).decode('utf-8') # decode('utf-8') - decode into string format (UTF-8) for storage
    
    conn = mysql.connect() # establishes connection to mySQL database
    cursor = conn.cursor() # cursor is created to execute SQL queries on the database

    # runs a SQL query to check if a user with given email already exists in users table. %s is placeholder for email value
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

    existing_user = cursor.fetchone() # fetches first record that matches email (if any)

    if existing_user: # if user exists, return JSON response error msg 400 status code
        return jsonify({"msg": "Account already exists"}), 400

    # executes SQL query to insert new user into users table with provided email & password
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_pswd))
    conn.commit() # commits transaction to database, saving changes
    conn.close() # closes database connection

    # sends successful response back to client with 201 status code (created)
    return jsonify({"msg": "Account creation succesful!"}), 201 

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json() # reads incoming JSON data in request body, converts to python dictionary
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"msg": "Email and password fields required"}), 400

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    # if no user is found or password doesnt match hashed pass in database (stored in user[2]) returns error response, 401 code (unauthorized)
    if not user or not bcrypt.check_password_hash(user[2], password):
        return jsonify({"msg": "Invalid email or password. Try again"}), 401

if __name__ == '__main__':
    app.run(debug=True)
