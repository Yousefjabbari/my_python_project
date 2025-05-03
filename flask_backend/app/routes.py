from flask import Blueprint, request, jsonify
from .utils import load_tasks, save_tasks

task_routes = Blueprint("task_routes", __name__)

@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@task_routes.route("/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks()
    data = request.json
    new_task = {
        "id": len(tasks) + 1 if tasks else 1,
        "title": data.get("title", "تسک بدون نام"),
        "done": data.get("done", False)
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            data = request.json
            task["title"] = data.get("title", task["title"])
            task["done"] = data.get("done", task["done"])
            save_tasks(tasks)
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        return jsonify({"error": "Task not found"}), 404
    save_tasks(new_tasks)
    return jsonify({"message": "Task deleted"}), 200

@task_routes.route("/reorder-tasks", methods=["PUT"])
def reorder_tasks():
    data = request.json
    if "tasks" not in data:
        return jsonify({"error": "Invalid data"}), 400
    tasks = data["tasks"]
    save_tasks(tasks)
    return jsonify({"message": "Tasks reordered successfully"}), 200
