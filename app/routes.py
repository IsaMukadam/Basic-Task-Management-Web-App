from flask import Blueprint, jsonify, request, render_template
from .models import db, Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def home():
    tasks = Task.query.all()  # Retrieve all tasks from the database
    return render_template('home.html', tasks=tasks)

@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    task_name = request.json.get('task')
    if task_name:
        new_task = Task(name=task_name)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'task': new_task.name}), 201
    return jsonify({'error': 'Task cannot be empty'}), 400

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()  # Retrieve all tasks
    return jsonify([{'id': task.id, 'name': task.name} for task in tasks])
