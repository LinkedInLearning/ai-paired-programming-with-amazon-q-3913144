from flask import Blueprint, jsonify, request
from models import create_task, get_all_tasks, update_task_status, delete_task, find_task_by_id

task_routes = Blueprint('tasks', __name__)

@task_routes.route('/', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({'error': 'Missing task description'}), 400

    task = create_task(data['description'])
    return jsonify(task), 201

@task_routes.route('/', methods=['GET'])
def get_tasks():
    return jsonify(get_all_tasks())

@task_routes.route('/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({'error': 'Missing task status'}), 400

    task = update_task_status(task_id, data['status'])
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)

@task_routes.route('/<task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    task = find_task_by_id(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    delete_task(task_id)
    return jsonify({'message': 'Task deleted'})
