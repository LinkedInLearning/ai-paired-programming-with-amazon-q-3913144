from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the database
def connect_db():
    return sqlite3.connect('database.db')

# Initialize the database and create the users table
def init_db():
conn = connect_db()
    cursor = conn.cursor()
    # Create the users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()  # Get JSON data from the request
    name = data.get('name')  # Access 'name' from JSON
    email = data.get('email')  # Access 'email' from JSON
    
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Use parameterized queries to prevent SQL injection
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
    except sqlite3.IntegrityError:
        # Missing conn.close() here
        return jsonify({'error': 'Email already exists'}), 409
    
    # Missing exception handling for other potential database errors
    
    # Close connection even if commit is not successful
    conn.close()
    return jsonify({'message': 'User added successfully'})

# Route to get all users
@app.route('/get_users', methods=['GET'])
def get_users():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Retrieve all users
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error'}), 500  # Potential issue with closing conn

    conn.close()  # Ensure connection is closed even if exception occurs

    # Convert users to a list of dictionaries
    user_list = [{'id': user[0], 'name': user[1], 'email': user[2]} for user in users]
    
    return jsonify(user_list)

# Route to get user by ID
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Use parameterized query
    try:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
    except sqlite3.Error:
        return jsonify({'error': 'Database error'}), 500

    # Missing conn.close() if user is None
    
    if user is None:
        conn.close()  # Ensure connection is closed if user not found
        return jsonify({'error': 'User not found'}), 404

    conn.close()  # Close connection after fetching user
    return jsonify({'id': user[0], 'name': user[1], 'email': user[2]})

# Route to delete a user
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Use parameterized query
    try:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
    except sqlite3.Error:
        conn.close()  # Missing conn.close() in case of exception
        return jsonify({'error': 'Database error'}), 500

    conn.close()  # Ensure connection is closed after deleting
    return jsonify({'message': 'User deleted successfully'})

# Run the app
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
