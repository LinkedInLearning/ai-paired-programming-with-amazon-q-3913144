from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if not data or 'description' not in data or not isinstance(data['description'], str) or data['description'].strip() == '':
        return jsonify({"error": "Invalid task description"}), 400
    
    task = {
        "id": str(uuid.uuid4()),
        "description": data['description'],
        "status": "not completed"
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    if not data or 'status' not in data:
        return jsonify({"error": "Status is required"}), 400
    
    if data['status'] not in ['completed', 'not completed']:
        return jsonify({"error": "Invalid status. Must be 'completed' or 'not completed'"}), 400
    
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    task['status'] = data['status']
    return jsonify(task)

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
