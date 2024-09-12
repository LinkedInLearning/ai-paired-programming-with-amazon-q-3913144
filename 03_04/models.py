import uuid

# In-memory data store for tasks
tasks = []

def create_task(description):
    task = {
        'id': str(uuid.uuid4()),  # Generate a unique ID for the task
        'description': description,
        'status': 'not completed'
    }
    tasks.append(task)
    return task

def get_all_tasks():
    return tasks

def find_task_by_id(task_id):
    return next((task for task in tasks if task['id'] == task_id), None)

def update_task_status(task_id, status):
    task = find_task_by_id(task_id)
    if task:
        task['status'] = status
    return task

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return tasks
