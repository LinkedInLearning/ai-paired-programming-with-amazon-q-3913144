from flask import Flask
from routes import task_routes

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(task_routes, url_prefix='/tasks')

if __name__ == '__main__':
    app.run(debug=True)
