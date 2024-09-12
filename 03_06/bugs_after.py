from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the database
def connect_db():
    return sqlite3.connect('database.db')

# Initialize the database and create the users table
def init_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        # Create the users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

# Route to add a new user
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ... (other code) ...

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
    except sqlite3.IntegrityError:
        logging.error(f"Email '{email}' already exists.")
        return jsonify({'error': 'Email already exists'}), 409
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

    logging.info(f"User '{name}' ({email}) added successfully.")
    return jsonify({'message': 'User added successfully'}), 201

# Route to get all users
@app.route('/get_users', methods=['GET'])
def get_users():
    with connect_db() as conn:
        cursor = conn.cursor()

        # Retrieve all users
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

    # Convert users to a list of dictionaries

    return jsonify(user_list)

# Route to get user by ID
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with connect_db() as conn:
        cursor = conn.cursor()

        # Use parameterized query
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

        user = cursor.fetchone()

    if user is None:
        return jsonify({'error': 'User not found'}), 404

# Route to delete a user
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with connect_db() as conn:
        cursor = conn.cursor()

        # Use parameterized query
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

    return jsonify({'message': 'User deleted successfully'})

# Run the app
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
